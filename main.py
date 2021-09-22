import tic_tac_toe
import textwrap as tw

ttt = tic_tac_toe.TicTacToe()

title_message = tw.dedent(
    f"""
    {50 * '*'}
    {19 *' '}TIC-TAC-TOE
    {50 * '*'}
    """)

if __name__ == '__main__':
    print(title_message)
    ttt.play_game()

