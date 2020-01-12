def convert_dates_to_seconds(date_init, date_end):
    import datetime


    date_init_list = date_init.split('/')
    date_end_list = date_end.split('/')

    date_init = datetime.date(
        day=int(date_init_list[0]),
        month=int(date_init_list[1]),
        year=int(date_init_list[2])
    )

    date_end = datetime.date(
        day=int(date_end_list[0]),
        month=int(date_end_list[1]),
        year=int(date_end_list[2])
    )

    if(date_end < date_init):
        print('data final menor que a atual, impossível continuar')
    else:
        date_sub = date_end - date_init
        hour_now = datetime.datetime.now().strftime('%H')
        minute_now = datetime.datetime.now().strftime('%M')

        dates_horus_now = float((date_sub.days*24) + int(hour_now) + (float(minute_now)/60))
        print('Data atual aproximada em segundos:',dates_horus_now*3600)


def main():
    print('CONVERSÃO DE DATAS PARA SEGUNDOS')
    print('='*33)
    print('\n')

    date_init_user = input(str('Informe uma data de início: '))
    date_end_user = input(str('Informe uma data de fim: '))

    convert_dates_to_seconds(date_init_user, date_end_user)


if __name__ == '__main__':
    main()
