#    Main Author(s): Marco Lau, Vatsal Bhatt, Martin Mathew Roy
#    Main Reviewer(s): Marco Lau

from a1_partc import Queue

def get_overflow_list(grid):
	#rows: len(grid)
	#columns: len(grid[0])
	# >2 for corners, >3 for edges, >4 everywhere else
	arr = []
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			if (x == 0 or x == (len(grid) - 1)) and (y == 0 or y == (len(grid[x]) - 1)):
				if abs(grid[x][y]) >= 2: arr.append((x, y))
			elif (x == 0) or (x == (len(grid) - 1)) or (y == 0) or (y == (len(grid[x]) - 1)):
				if abs(grid[x][y]) >= 3: arr.append((x, y))
			else:
				if abs(grid[x][y]) >= 4: arr.append((x, y))
	if (len(arr)):
		return arr
	else:
		return None

def overflow(grid, a_queue):
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    spill_detected = False
    spill_count = 0
    mixed_signals = scan_for_dual_signs(grid)

    spill_sites = get_overflow_list(grid)

    if spill_sites is None or not mixed_signals:
        return 0

    original_matrix = [each_row.copy() for each_row in grid]
    for x, y in spill_sites:
        grid[x][y] = 0

    for x, y in spill_sites:
        current_sign = 1 if original_matrix[x][y] > 0 else -1
        spill_detected = True

        # Adjust surrounding cells
        if y < grid_cols - 1:  # Right
            grid[x][y + 1] = (abs(grid[x][y + 1]) + 1) * current_sign
        if y > 0:  # Left
            grid[x][y - 1] = (abs(grid[x][y - 1]) + 1) * current_sign
        if x > 0:  # Up
            grid[x - 1][y] = (abs(grid[x - 1][y]) + 1) * current_sign
        if x < grid_rows - 1:  # Down
            grid[x + 1][y] = (abs(grid[x + 1][y]) + 1) * current_sign

    if spill_detected:
        a_queue.enqueue([each_row.copy() for each_row in grid])
        spill_count = 1 + overflow(grid, a_queue)

    return spill_count


def scan_for_dual_signs(grid):
    has_positive = False
    has_negative = False
    for line in grid:
        for item in line:
            if item > 0:
                has_positive = True
            elif item < 0:
                has_negative = True
            if has_positive and has_negative:
                return True
    return False
