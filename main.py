from time import time
from terminal_input import Terminal_Input
from land_BFS import BarrenLandBFS


if __name__ == '__main__':
    params = Terminal_Input()

    print("--- Breath First Search ---")
    start = time()
    bfs = BarrenLandBFS(params.coordinates,params.x, params.y)
    result = bfs.find_fertile_areas()
    end = time()
    print("--- Fertile Land--- :")
    for plot in result:
        print(plot, end=" ")
    print("\nProcess Time (ms): {0:.15f}".format((end - start)*1000))
    print()
    if params.visualizations:
        bfs.display_land()




