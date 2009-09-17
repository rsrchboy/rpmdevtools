AC_INIT(rpmdevtools, 7.5)
AM_INIT_AUTOMAKE

AC_PROG_SED

AC_PATH_PROG([HELP2MAN], [help2man])
if test -z "$HELP2MAN" ; then
    AC_MSG_ERROR([help2man is required])
fi

AC_PATH_PROG([POD2MAN], [pod2man])
if test -z "$POD2MAN" ; then
    AC_MSG_ERROR([pod2man is required])
fi

AC_OUTPUT(
Makefile
devscripts/Makefile
devscripts/scripts/Makefile
emacs/Makefile
qa-robot/Makefile
)
