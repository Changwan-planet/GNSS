PROGRAM GNSS_ARR
IMPLICIT NONE

CHARACTER (LEN=255) :: cwd
CHARACTER (LEN=255) :: INPUT_PATH
CHARACTER (LEN=255) :: OUTPUT_PATH
CHARACTER (LEN=20) :: IFN
CHARACTER (LEN=20) :: OFN


INTEGER, PARAMETER :: ROWS = 602
INTEGER, PARAMETER :: COL = 4
INTEGER :: I, J

REAL*8, DIMENSION(ROWS,COL) :: ELE_MTX
!REAL*8, DIMENSION(COL,ROWS) :: ELE_MTX

CALL getcwd(cwd)
WRITE(*,*) TRIM(cwd)
IFN = "/elevation.txt"
OFN = "/elevation_fortran.txt"
!FN2 = TRIM(FN)

INPUT_PATH=TRIM(cwd)//IFN
PRINT *, INPUT_PATH
OUTPUT_PATH=TRIM(cwd)//OFN
PRINT *, INPUT_PATH


OPEN(UNIT=10, FILE=INPUT_PATH, ACCESS='STREAM',STATUS='OLD', ACTION='READ')
OPEN(UNIT=20, FILE=OUTPUT_PATH, ACCESS='STREAM',STATUS='OLD', ACTION='WRITE')


READ(10) ELE_MTX

I=583
J=3
PRINT *, "I=",I, "J=",J, ELE_MTX(I,J)


DO J=1,COL
   !PRINT *, "I=",I, "J=",J,ELE_MTX(I,J)
   WRITE(20) (ELE_MTX(I,J), I=1,ROWS) 
END DO


END PROGRAM GNSS_ARR
