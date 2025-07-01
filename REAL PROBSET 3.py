def relationship_status(from_member, to_member, social_graph):
    from_following = social_graph[from_member]["following"]
    to_following = social_graph[to_member]["following"]
    if from_member in to_following and to_member in from_following:
        return 'friends'
    elif from_member in to_following and to_member not in from_following:
        return 'followed by'
    elif from_member not in to_following and to_member in from_following:
        return 'follower'
    else:
        return 'no relationship'
    

def tic_tac_toe(board):
    length = len(board)
    
    for row in range(length):
        if all(board[row][c] == board[row][0] and board[row][0] != '' for c in range(length)):
            return board[row][0]
    
    for col in range(length):
        if all(board[r][col] == board[0][col] and board[0][col] != '' for r in range(length)):
            return board[0][col]
    
    if all(board[i][i] == board[0][0] and board[0][0] != '' for i in range(length)):
        return board[0][0]
    
    if all(board[i][length - i - 1] == board[0][length - 1] and board[0][length - 1] != '' for i in range(length)):
        return board[0][length - 1]
    return 'NO WINNER'


def eta(first_stop, second_stop, route_map):
    eta = 0
    current_stop = first_stop
    visited = set()
    while True:
        for (start, end), data in route_map.items():
            if start == current_stop:
                eta += data['travel_time_mins']
                current_stop = end
                if current_stop == second_stop:
                    return eta
               
                if (start, end) in visited:
                    return -1
                visited.add((start, end))
                break
    