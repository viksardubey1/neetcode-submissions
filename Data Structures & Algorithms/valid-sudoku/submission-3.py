class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        sub_boxes = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue

                sub_box_val = (r//3) + (c//3) * 3
                
                if (value in rows[r] or value in columns[c] or value in sub_boxes[sub_box_val]):
                    return False
            
                rows[r].add(value)
                columns[c].add(value)
                sub_boxes[sub_box_val].add(value)
        return True
        