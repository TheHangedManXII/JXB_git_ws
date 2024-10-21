#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/sdfg/JXB_git_ws/src/easy_handeye-master/easy_handeye"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/sdfg/JXB_git_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/sdfg/JXB_git_ws/install/lib/python3/dist-packages:/home/sdfg/JXB_git_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/sdfg/JXB_git_ws/build" \
    "/usr/bin/python3" \
    "/home/sdfg/JXB_git_ws/src/easy_handeye-master/easy_handeye/setup.py" \
    egg_info --egg-base /home/sdfg/JXB_git_ws/build/easy_handeye-master/easy_handeye \
    build --build-base "/home/sdfg/JXB_git_ws/build/easy_handeye-master/easy_handeye" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/sdfg/JXB_git_ws/install" --install-scripts="/home/sdfg/JXB_git_ws/install/bin"