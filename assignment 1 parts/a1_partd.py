
from maze import Maze



def find_path(maze, from_cell, to_cell):
    num_rows = maze.get_num_rows()
    num_cols = maze.get_num_cols()

    def recursive_find(current_cell, path):
        if current_cell == to_cell:
            return path + [current_cell]

        maze.mark_cell(current_cell) 
        neighbors = [maze.get_left(current_cell), maze.get_right(current_cell),
                     maze.get_up(current_cell), maze.get_down(current_cell)]
        
        for neighbor in neighbors:
            if neighbor is not None and not maze.get_is_marked(neighbor):
                new_path = recursive_find(neighbor, path + [current_cell])
                if new_path:
                    return new_path
        
        maze.unmark_cell(current_cell) 
        return None

    initial_path = recursive_find(from_cell, [])
    return initial_path




