def TowerOfHanoi(n , lef_rod, mid_rod, rig_rod):

    if n==1:

        print ("Move disk 1 from lef_rod",lef_rod,"to mid_rod",mid_rod)

        return

    TowerOfHanoi(n-1, lef_rod, rig_rod, mid_rod)

    print ("Move disk",n,"from lef_rod",lef_rod,"to mid_rod",mid_rod)

    TowerOfHanoi(n-1, rig_rod, mid_rod, lef_rod)
         
n = 4

TowerOfHanoi(n,'A','B','C')