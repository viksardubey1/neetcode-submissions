class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range((9))]
        columns = [set() for i in range((9))]
        sub_boxes = [set() for i in range((9))]

        for row in range(9):
            for column in range(9):
                val = board[row][column]

                if val == ".":
                    continue

                sub_box = row//3 + column//3 * 3

                if (val in rows[row]) or (val in columns[column]) or (val in sub_boxes[sub_box]):
                    return False
                
                rows[row].add(val)
                columns[column].add(val)
                sub_boxes[sub_box].add(val)
        
        return True
        