DO I = 1, DIS
   ROWS2(I) = ROWS + Shift_GPRelev_FLIP(I)
   PRINT *, I, Shift_GPRelev_FLIP(I), ROWS2(I)
END DO

MAX_SHIFT = MAXVAL(Shift_GPRelev_FLIP)
MAX_ROWS2 = MAXVAL(ROWS2)
PRINT *, "MAX_SHIFT=", MAX_SHIFT
PRINT *, "MAX_ROWS2=", MAX_ROWS2

ALLOCATE(BSCAN_GC_GNC(DIS,TRA,MAX_ROWS2))
ALLOCATE(BSCAN_GC_GNC2(DIS,TRA,MAX_ROWS2))
ALLOCATE(BSCAN_GC_GNC3(DIS,TRA,MAX_ROWS2))
ALLOCATE(BSCAN_GC_GNC4(DIS,TRA,MAX_ROWS2))

!====================
BSCAN_GC_GNC = 0.0
!====================

!=====SIZE UP====GEOMORPHIC CORRECTION-1==============
DO X = 1, DIS
DO Y = 1, TRA
DO Z = 1, ROWS

   BSCAN_GC_GNC(X,Y, (Z+MAX_SHIFT)) = BSCAN_GC_FLIP(X,Y,Z)

END DO
END DO
END DO 
!====================================================


!=====SHIFT=====GEOMORPHIC CORRECTION-2==============
DO X = 1, DIS
DO Y = 1, TRA
DO Z = MAX_SHIFT+1,MAX_ROWS2
   BSCAN_GC_GNC2(X,Y,(Z-Shift_GPRelev_FLIP(X)) )= BSCAN_GC_GNC(X,Y,Z)
END DO
END DO
END DO 
!====================================================


!++++++++++++++++++ONLY CHANGE THIS PART+++++++++++++
CUT_U = MAX_SHIFT + 35 !CUT UP
CUT_D = CUT_U+100      !CUT DOWN
!++++++++++++++++++++++++++++++++++++++++++++++++++++


!=====CUT DOWN=======GEOMORPHIC CORRECTION-3=========
BSCAN_GC_GNC3 = 1.0

DO X = 1, DIS
DO Y = 1, TRA
DO Z = 1,CUT_D-Shift_GPRelev_FLIP(X)
   BSCAN_GC_GNC3(X,Y,Z)= BSCAN_GC_GNC2(X,Y,Z)
END DO
END DO
END DO 
!====================================================

!=====CUT UP=======GEOMORPHIC CORRECTION-3=========
BSCAN_GC_GNC4 = 1.0

DO X = 1, DIS
DO Y = 1, TRA
DO Z = CUT_U-Shift_GPRelev_FLIP(X), MAX_ROWS2
   BSCAN_GC_GNC4(X,Y,Z)= BSCAN_GC_GNC3(X,Y,Z)
END DO
END DO
END DO 
!====================================================


