from TV import TV


def main():
    tv1 = TV()
    tv1.turn_on()
    tv1.set_channel(30)
    tv1.set_volume_level(3)

    tv2 = TV()
    tv2.turn_on()
    tv2.channel_up()
    tv2.channel_up()
    tv2.volume_up()

    print(tv1.get_channel(), "\t", tv1.get_volume_level())
    print(tv2.get_channel(), "\t", tv2.get_volume_level())


main()
