AC_INIT(rpmdevtools, 5.3)
AM_INIT_AUTOMAKE
AC_PATH_PROG([HELP2MAN], [help2man], [no])
if test "$HELP2MAN" = "no" ; then
    AC_MSG_ERROR([help2man is required])
fi
AC_PATH_PROG([WGET], [wget], [no])
if test "$WGET" = "no" ; then
    AC_MSG_ERROR([wget is required])
fi
AC_OUTPUT(
Makefile
emacs/Makefile
qa-robot/Makefile
test/Makefile
)
