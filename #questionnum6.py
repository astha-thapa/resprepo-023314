#questionnum6
def heuristic(board, player):
    opponent = 'O' if player == 'X' else 'X'
    
    def count_open_lines(current_player, current_opponent):
        count = 0
        # Define all 8 possible winning lines
        lines = []
        # Rows
        lines.extend([row for row in board])
        # Columns
        lines.extend([[board[j][i] for j in range(3)] for i in range(3)])
        # Diagonals
        lines.append([board[i][i] for i in range(3)])
        lines.append([board[i][2 - i] for i in range(3)])
        
        # A line is open if the opponent has zero marks in it
        for line in lines:
            if all(cell != current_opponent for cell in line):
                count += 1
        return count

    # Calculate e(p) = Open(Player) - Open(Opponent)
    open_p = count_open_lines(player, opponent)
    open_opp = count_open_lines(opponent, player)
    
    return open_p - open_opp

# Example usage from your prompt
board = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', ' ', ' ']
]

player = 'X'
h_value = heuristic(board, player)
print(f"Heuristic value for player {player} is: {h_value}")
#output:
#Heuristic value for player X is: 2         