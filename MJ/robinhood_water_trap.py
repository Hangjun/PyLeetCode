def print_terrain(terrain, water):
    max_height = max(th + wh for th, wh in zip(terrain, water))
    for h in range(max_height, 0, -1):
        for i in range(len(terrain)):
            if terrain[i] + water[i] < h:
                print(" "),
            elif terrain[i] < h:
                print("W"),
            else:
                print("B"),
        print('\n'),


def drop_water(terrain, locations):
    if not terrain:
        return
    extended_terrain = [-1]
    extended_terrain.extend(terrain)
    extended_terrain.append(-1)
    water = [0 for _ in range(len(extended_terrain))]
    extended_locations = [location+1 for location in locations]
    for location in extended_locations:
        drop_location = location
        left = right = location
        # move to the left first
        while left >= 1:
            if extended_terrain[left-1] + water[left-1] > extended_terrain[left] + water[left]:
                break
            left -= 1
        if extended_terrain[left] + water[left] < extended_terrain[location] + water[location]:
            drop_location = left
        else:
            # try move to the right next
            while right < len(extended_terrain)-1:
                if extended_terrain[right+1] + water[right+1] > extended_terrain[right] + water[right]:
                    break
                right += 1
            if extended_terrain[right] + water[right] < extended_terrain[location] + water[location]:
                drop_location = right
        water[drop_location] += 1

    print_terrain(extended_terrain[1:-1], water[1:-1])


if __name__ == '__main__':
    terrain1 = [2, 0, 3, 5, 1, 2]
    drop_water(terrain1, [4, 4, 1, 1, 1, 1])
    print('---------')
    terrain2 = [1, 1, 1, 1, 1, 1]
    drop_water(terrain2, [2, 3, 4, 0])
    print('---------')
    terrain3 = [2, 1, 1, 1, 2]
    drop_water(terrain3, [1, 1, 2, 3, 3])
