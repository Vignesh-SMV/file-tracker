def get_info(receiver_mail):
    from Google import main

    import socket
    import platform
    from datetime import datetime
    date_time = datetime.now()

    # Get the hostname and IP address
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # Get system information
    system_info = platform.system()

    year = date_time.year
    month = date_time.month
    date = date_time.day

    hour = date_time.hour
    minute = date_time.minute
    second = date_time.second

    # Display the information
    '''print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    print(f"System: {system_info}")
    print(f"{date}-{month}-{year} | {hour}:{minute}:{second}")'''
    info=f"-------------------details-----------------------------------" \
         f"\n Host name :{hostname}\n IP Address:{ip_address}\n system info :{system_info} " \
         f"\n Date : {date}-{month}-{year} " \
         f"\n Time {hour}:{minute}:{second}"
    main(receiver_mail,info)
    print("code file executed")

