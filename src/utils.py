from datetime import timedelta

def convert_time(quarter, time) -> int:
        time_minutes, time_seconds = time.split(':')
        if quarter != 'OT':
                converted_quater = timedelta(minutes=(60-(15*int(quarter))))
        else:
                converted_quater = timedelta(10)
        converted_time = timedelta(minutes=int(time_minutes), seconds=int(time_seconds))
        total_time = converted_quater + converted_time
        sec = int(total_time.seconds)
        return sec


def get_outcome(score_a, score_b, a=None, b=None):
        if score_a > score_b:
                outcome = 1 #Team A wins
                if a != None:
                        a.wins += 1
                        b.losses += 1

        elif score_a < score_b:
                outcome = -1 #Team B wins
                if a != None:
                        a.losses += 1
                        b.wins += 1

        elif score_a == score_b:
                outcome = 0.5 #draw
                if a != None:
                        a.ties += 1
                        b.ties += 1
        else:
            raise ValueError('Somethings messed up fam')

        return outcome