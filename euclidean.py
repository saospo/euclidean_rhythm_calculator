from argparse import ArgumentParser


def concatenate_strings(array: list) -> str:
    output = ""
    for x in array:
        output += x
    return output


# this implements a tool which outputs a canonical Euclidean rhythm when given inputs of n time steps and k beats, as well as an offset (rotation) of offset time steps
# I also keep a few functions I wrote down at the bottom, including an implementation of the Euclidean algorithm
def create_rhythm_string(k: int, n: int, offset: int) -> str:
    inverted = True if k < 0 else False

    beat_record_string = "x" * abs(k) + "." * (n - abs(k))
    beat_record: list = [x for x in beat_record_string]
    print("first beat record", beat_record)

    while len(beat_record) > 1:
        first_string = beat_record[0]
        count_first_string = len([x for x in beat_record if x == first_string])

        if count_first_string <= 1 or len(beat_record) - count_first_string <= 1:
            output = concatenate_strings(beat_record)
            break

        # generally, after every pass we want to have the beat string array have only 2 kinds of items on it. We want to take from
        # the second item and add to the first using those elements of the second until either we run out of the first string or use all the second strings
        # to do this, we can take the minimum of the length of the beat_record less the number of type-1 strings, or we can do the operation
        # a number of times equal to the number of type 1 strings
        # it just so happens that this will follow the pattern of the r values coming from the Euclidean algorithm for this set of k and n.
        # so we could run our Euclidean algorithm function, or we can just do it this way and have the overlap with the Euclidean algorithm
        # be a happy accident. I'm going with the second option here.
        for i in range(min(count_first_string, len(beat_record)-count_first_string)):
            to_add = beat_record.pop(-1)
            beat_record[i] = beat_record[i] + to_add

    if inverted:
        output = output.translate(str.maketrans('x.', '.x'))

    return output[-offset:] + output[:-offset]


if __name__ == "__main__":
    parser = ArgumentParser(prog="euclidean",
                                     description='given numerical inputs returns a euclidean rhythm, distribute k beats over n time steps with offset steps of right rotation.')
    parser.add_argument('k', type=int, help='number of beats to distribute. must be an integer whose absolute value is less than number of time steps, and not 0')
    parser.add_argument('n', type=int, help='number of time steps. must be a positive integer greater than the number of beats')
    parser.add_argument('offset', nargs='?', default=0, type=int, help='number of time steps to offset. can be negative (left rotation). abs(offset) + abs(k) must be less than or equal to the number of time steps')

    try:
        args = parser.parse_args()
        if args.k == 0 or args.n <= 0:
            raise ValueError
        elif abs(args.k) > args.n:
            raise ValueError
        elif abs(args.offset) > args.n:
            raise ValueError
        elif abs(args.offset) + abs(args.k) >= args.n:
            raise ValueError

        print(create_rhythm_string(args.k, args.n, args.offset))

    except ValueError:
        parser.print_help()


def get_q_and_r(a, b):
    """returns list of qs and rs, leaves out offset since the offset is just applied before algorithm runs"""
    initial_rs = [a, b]
    initial_qs = []

    total = a
    multiplier = b
    q = int(total / multiplier)
    r = total - q * multiplier
    total = multiplier
    multiplier = r
    initial_rs.append(r)
    initial_qs.append(q)

    while r > 0:
        r = int(total % multiplier)
        q = int((total - r) / multiplier)
        total = multiplier
        multiplier = r

        initial_rs.append(r)
        initial_qs.append(q)

    final_rs = initial_rs[1:]
    final_qs = initial_qs

    print(final_rs)
    print(final_qs)

    return final_rs, final_qs


def create_rhythm_string(k: int, n: int, offset: int) -> str:
    rs, qs = get_q_and_r(n, k)

    print("rs=", rs)

    beat_record: list = ["x" * k + "." * (n - k)]

    print("first beat record", beat_record)

    t_index = 0
    t = rs[t_index]
    lengths = [len(x) for x in beat_record]
    max_length = max(lengths)

    print("t=", t, "max_length=", max_length, "t_index=", t_index)

    # how this works:
    # we chop t (r[n]) off of every row of max length. so we need to identify max length rows
    # we stop when
    while max_length > t > 0:
        # for every column in beat_record that ***currently exists***: new ones get appended to the end
        for i in range(len(beat_record)):
            if len(beat_record[i]) == max_length:
                beat_record.append(beat_record[i][-t:])
                beat_record[i] = beat_record[i][:-t]

        print(beat_record)

        lengths = [len(x) for x in beat_record]
        max_length = max(lengths)

        t_index += 1
        t = rs[t_index]
        print("max_length=", max_length, "t=", t)

    output_beat_string = ""
    for i in range(max_length):
        print(beat_record)
        beat_record = [x for x in beat_record if len(x) > i]
        for j in beat_record:
            output_beat_string += j[i]

    output_beat_string = output_beat_string[-offset:] + output_beat_string[offset:-offset] + output_beat_string[:offset]

    return output_beat_string
