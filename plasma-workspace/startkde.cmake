#!/bin/sh
#
#  DEFAULT KDE STARTUP SCRIPT ( @PROJECT_VERSION@ )
#

if test "x$1" = x--failsafe; then
    KDE_FAILSAFE=1 # General failsafe flag
    KWIN_COMPOSE=N # Disable KWin's compositing
    export KWIN_COMPOSE KDE_FAILSAFE
fi

# When the X server dies we get a HUP signal from xinit. We must ignore it
# because we still need to do some cleanup.
trap 'echo GOT SIGHUP' HUP

# we have to unset this for Darwin since it will screw up KDE's dynamic-loading
unset DYLD_FORCE_FLAT_NAMESPACE

qdbus=qdbus-qt5

# See http://bugzilla.redhat.com/537609 , a naive attempt to drop dep 
# on xmessage and allow alternatives like zenity.  
message() {
  xmessage -geometry 500x100 "$1" > /dev/null 2>/dev/null || \
    zenity --info --text="$1" > /dev/null 2>/dev/null ||:
  return $?
}

# Check if a KDE session already is running and whether it's possible to connect to X
kcheckrunning
kcheckrunning_result=$?
if test $kcheckrunning_result -eq 0 ; then
	echo "KDE seems to be already running on this display."
	message "KDE seems to be already running on this display." > /dev/null 2>/dev/null
	exit 1
elif test $kcheckrunning_result -eq 2 ; then
	echo "\$DISPLAY is not set or cannot connect to the X server."
        exit 1
fi

# Boot sequence:
#
# kdeinit is used to fork off processes which improves memory usage
# and startup time.
#
# * kdeinit starts klauncher first.
# * Then kded is started. kded is responsible for keeping the sycoca
#   database up to date. When an up to date database is present it goes
#   into the background and the startup continues.
# * Then kdeinit starts kcminit. kcminit performs initialisation of
#   certain devices according to the user's settings
#
# * Then ksmserver is started which takes control of the rest of the startup sequence

# We need to create config folder so we can write startupconfigkeys
if [  ${XDG_CONFIG_HOME} ]; then
  configDir=$XDG_CONFIG_HOME;
else
  configDir=${HOME}/.config; #this is the default, http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
fi

mkdir -p $configDir

#This is basically setting defaults so we can use them with kstartupconfig5
cat >$configDir/startupconfigkeys <<EOF
kcminputrc Mouse cursorTheme 'breeze_cursors'
kcminputrc Mouse cursorSize ''
ksplashrc KSplash Theme Breeze
ksplashrc KSplash Engine KSplashQML
kdeglobals KScreen ScaleFactor 1
kcmfonts General forceFontDPI 0
EOF

# preload the user's locale on first start
plasmalocalerc=$configDir/plasma-localerc
test -f $plasmalocalerc || {
cat >$plasmalocalerc <<EOF
[Formats]
LANG=$LANG
EOF
}

# export LC_* variables set by kcmshell5 formats into environment
# so it can be picked up by QLocale and friends.
exportformatssettings=$configDir/plasma-locale-settings.sh

test -f $exportformatssettings || {
cat >$exportformatssettings <<EOF
export LANG=$LANG
export LC_MESSAGES=$LANG
export LC_NUMERIC=$LANG
export LC_TIME=$LANG
export LC_MONETARY=$LANG
export LC_MEASUREMENT=$LANG
export LC_COLLATE=$LANG
export LC_CTYPE=$LANG
EOF
}

test -f $exportformatssettings && {
    . $exportformatssettings
}

kstartupconfig5
returncode=$?
if test $returncode -ne 0; then
    message "kstartupconfig5 does not exist or fails. The error code is $returncode. Check your installation."
    exit 1
fi
[ -r $configDir/startupconfig ] && . $configDir/startupconfig

if test "$kdeglobals_kscreen_scalefactor" -ne 1; then
    export QT_DEVICE_PIXEL_RATIO=$kdeglobals_kscreen_scalefactor
fi

# XCursor mouse theme needs to be applied here to work even for kded or ksmserver
if test -n "$kcminputrc_mouse_cursortheme" -o -n "$kcminputrc_mouse_cursorsize" ; then
    @EXPORT_XCURSOR_PATH@

    kapplymousetheme "$kcminputrc_mouse_cursortheme" "$kcminputrc_mouse_cursorsize"
    if test $? -eq 10; then
        XCURSOR_THEME=breeze_cursors
        export XCURSOR_THEME
    elif test -n "$kcminputrc_mouse_cursortheme"; then
        XCURSOR_THEME="$kcminputrc_mouse_cursortheme"
        export XCURSOR_THEME
    fi
    if test -n "$kcminputrc_mouse_cursorsize"; then
        XCURSOR_SIZE="$kcminputrc_mouse_cursorsize"
        export XCURSOR_SIZE
    fi
fi

if test "$kcmfonts_general_forcefontdpi" -ne 0; then
    xrdb -quiet -merge -nocpp <<EOF
Xft.dpi: $kcmfonts_general_forcefontdpi
EOF
fi

dl=$DESKTOP_LOCKED
unset DESKTOP_LOCKED # Don't want it in the environment

ksplash_pid=
if test -z "$dl"; then
  # the splashscreen and progress indicator
  case "$ksplashrc_ksplash_engine" in
    KSplashQML)
      ksplash_pid=`ksplashqml "${ksplashrc_ksplash_theme}" --pid`
      ;;
    None)
      ;;
    *)
      ;;
  esac
fi

# Source scripts found in <config locations>/plasma-workspace/env/*.sh
# (where <config locations> correspond to the system and user's configuration
# directories, as identified by Qt's qtpaths,  e.g.  $HOME/.config
# and /etc/xdg/ on Linux)
#
# This is where you can define environment variables that will be available to
# all KDE programs, so this is where you can run agents using e.g. eval `ssh-agent`
# or eval `gpg-agent --daemon`.
# Note: if you do that, you should also put "ssh-agent -k" as a shutdown script
#
# (see end of this file).
# For anything else (that doesn't set env vars, or that needs a window manager),
# better use the Autostart folder.

# TODO: Use GenericConfigLocation once we depend on Qt 5.4
scriptpath=`qtpaths --paths ConfigLocation | tr ':' '\n' | sed 's,$,/plasma-workspace,g'`

# Add /env/ to the directory to locate the scripts to be sourced
for prefix in `echo $scriptpath`; do
  for file in "$prefix"/env/*.sh; do
    test -r "$file" && . "$file"
  done
done

# Set a left cursor instead of the standard X11 "X" cursor, since I've heard
# from some users that they're confused and don't know what to do. This is
# especially necessary on slow machines, where starting KDE takes one or two
# minutes until anything appears on the screen.
#
# If the user has overwritten fonts, the cursor font may be different now
# so don't move this up.
#
xsetroot -cursor_name left_ptr

echo 'startkde: Starting up...'  1>&2

# Make sure that the KDE prefix is first in XDG_DATA_DIRS and that it's set at all.
# The spec allows XDG_DATA_DIRS to be not set, but X session startup scripts tend
# to set it to a list of paths *not* including the KDE prefix if it's not /usr or
# /usr/local.
if test -z "$XDG_DATA_DIRS"; then
    XDG_DATA_DIRS="@CMAKE_INSTALL_PREFIX@/@SHARE_INSTALL_PREFIX@:/usr/share:/usr/local/share"
fi
export XDG_DATA_DIRS

# Make sure that D-Bus is running
# D-Bus autolaunch is broken
if test -z "$DBUS_SESSION_BUS_ADDRESS" ; then
    eval `dbus-launch --sh-syntax --exit-with-session`
fi
if $qdbus >/dev/null 2>/dev/null; then
    : # ok
else
    echo 'startkde: Could not start D-Bus. Can you call qdbus?'  1>&2
    test -n "$ksplash_pid" && kill "$ksplash_pid" 2>/dev/null
    message "Could not start D-Bus. Can you call qdbus?"
    exit 1
fi


# Mark that full KDE session is running (e.g. Konqueror preloading works only
# with full KDE running). The KDE_FULL_SESSION property can be detected by
# any X client connected to the same X session, even if not launched
# directly from the KDE session but e.g. using "ssh -X", kdesu. $KDE_FULL_SESSION
# however guarantees that the application is launched in the same environment
# like the KDE session and that e.g. KDE utilities/libraries are available.
# KDE_FULL_SESSION property is also only available since KDE 3.5.5.
# The matching tests are:
#   For $KDE_FULL_SESSION:
#     if test -n "$KDE_FULL_SESSION"; then ... whatever
#   For KDE_FULL_SESSION property:
#     xprop -root | grep "^KDE_FULL_SESSION" >/dev/null 2>/dev/null
#     if test $? -eq 0; then ... whatever
#
# Additionally there is (since KDE 3.5.7) $KDE_SESSION_UID with the uid
# of the user running the KDE session. It should be rarely needed (e.g.
# after sudo to prevent desktop-wide functionality in the new user's kded).
#
# Since KDE4 there is also KDE_SESSION_VERSION, containing the major version number.
# Note that this didn't exist in KDE3, which can be detected by its absense and
# the presence of KDE_FULL_SESSION.
#
KDE_FULL_SESSION=true
export KDE_FULL_SESSION
xprop -root -f KDE_FULL_SESSION 8t -set KDE_FULL_SESSION true

KDE_SESSION_VERSION=5
export KDE_SESSION_VERSION
xprop -root -f KDE_SESSION_VERSION 32c -set KDE_SESSION_VERSION 5

KDE_SESSION_UID=`id -ru`
export KDE_SESSION_UID

XDG_CURRENT_DESKTOP=KDE
export XDG_CURRENT_DESKTOP

# At this point all the environment is ready, let's send it to kwalletd if running
if test -n "$PAM_KWALLET_LOGIN" ; then
    env | socat STDIN UNIX-CONNECT:$PAM_KWALLET_LOGIN
fi
# ...and also to kwalletd5
if test -n "$PAM_KWALLET5_LOGIN" ; then
    env | socat STDIN UNIX-CONNECT:$PAM_KWALLET5_LOGIN
fi

# At this point all environment variables are set, let's send it to the DBus session server to update the activation environment
@CMAKE_INSTALL_FULL_LIBEXECDIR@/ksyncdbusenv
if test $? -ne 0; then
  # Startup error
  echo 'startkde: Could not sync environment to dbus.'  1>&2
  test -n "$ksplash_pid" && kill "$ksplash_pid" 2>/dev/null
  message "Could not sync environment to dbus."
  exit 1
fi

@CMAKE_INSTALL_FULL_LIBEXECDIR_KF5@/start_kdeinit_wrapper --kded +kcminit_startup
if test $? -ne 0; then
  # Startup error
  echo 'startkde: Could not start kdeinit5. Check your installation.'  1>&2
  test -n "$ksplash_pid" && kill "$ksplash_pid" 2>/dev/null
  message "Could not start kdeinit5. Check your installation."
  exit 1
fi

# finally, give the session control to the session manager
# see kdebase/ksmserver for the description of the rest of the startup sequence
# if the KDEWM environment variable has been set, then it will be used as KDE's
# window manager instead of kwin.
# if KDEWM is not set, ksmserver will ensure kwin is started.
# kwrapper5 is used to reduce startup time and memory usage
# kwrapper5 does not return useful error codes such as the exit code of ksmserver.
# We only check for 255 which means that the ksmserver process could not be
# started, any problems thereafter, e.g. ksmserver failing to initialize,
# will remain undetected.
test -n "$KDEWM" && KDEWM="--windowmanager $KDEWM"
# If the session should be locked from the start (locked autologin),
# lock now and do the rest of the KDE startup underneath the locker.
KSMSERVEROPTIONS=""
test -n "$dl" && KSMSERVEROPTIONS=" --lockscreen"
kwrapper5 ksmserver $KDEWM $KSMSERVEROPTIONS
if test $? -eq 255; then
  # Startup error
  echo 'startkde: Could not start ksmserver. Check your installation.'  1>&2
  test -n "$ksplash_pid" && kill "$ksplash_pid" 2>/dev/null
  message "Could not start ksmserver. Check your installation."
fi

wait_drkonqi=`kreadconfig5 --file startkderc --group WaitForDrKonqi --key Enabled --default true`

if test x"$wait_drkonqi"x = x"true"x ; then
    # wait for remaining drkonqi instances with timeout (in seconds)
    wait_drkonqi_timeout=`kreadconfig5 --file startkderc --group WaitForDrKonqi --key Timeout --default 900`
    wait_drkonqi_counter=0
    while $qdbus | grep "^[^w]*org.kde.drkonqi" > /dev/null ; do
        sleep 5
        wait_drkonqi_counter=$((wait_drkonqi_counter+5))
        if test "$wait_drkonqi_counter" -ge "$wait_drkonqi_timeout" ; then
            # ask remaining drkonqis to die in a graceful way
            $qdbus | grep 'org.kde.drkonqi-' | while read address ; do
                $qdbus "$address" "/MainApplication" "quit"
            done
            break
        fi
    done
fi

echo 'startkde: Shutting down...'  1>&2
# just in case
test -n "$ksplash_pid" && kill "$ksplash_pid" 2>/dev/null

# just in case, avoid a qsqldatabase->close crash issue, by cjacker.
#https://bugreports.qt.io/browse/QTBUG-35977
kactivitymanagerd stop 1>&2 

# Clean up
kdeinit5_shutdown

# just in case, by cjacker.
killall kuiserver5 2>/dev/null 
killall kwalletd5 2>/dev/null
killall kglobalaccel5 2>/dev/null

echo 'startkde: Running shutdown scripts...'  1>&2

# Run scripts found in <config locations>/plasma-workspace/shutdown
for prefix in `echo "$scriptpath"`; do
  for file in `ls "$prefix"/shutdown 2> /dev/null | egrep -v '(~|\.bak)$'`; do
    test -x "$prefix/shutdown/$file" && "$prefix/shutdown/$file"
  done
done

unset KDE_FULL_SESSION
xprop -root -remove KDE_FULL_SESSION
unset KDE_SESSION_VERSION
xprop -root -remove KDE_SESSION_VERSION
unset KDE_SESSION_UID

echo 'startkde: Done.'  1>&2
