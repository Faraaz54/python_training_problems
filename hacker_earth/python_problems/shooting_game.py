for _ in xrange(int(raw_input())):
    ammo, obstacles = raw_input().split()
    ammo1 = int(ammo)
    obs_list = raw_input().split()
    finish = True
    pos = 0

    for i in xrange(int(obstacles)):
        if obs_list[i] == '1':
            ammo1 += 2
        else:
            ammo1 -= 1

        if ammo1 == 0 and i < int(obstacles)-1:
            finish = False
            pos = i+1
            break
    if finish:
        print 'Yes', ammo1
    else:
        print 'No', pos










