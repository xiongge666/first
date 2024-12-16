import serial

# 配置串口参数
port = 'COM104'  # 根据实际情况设置串口端口
baudrate = 921600  # 根据实际情况设置波特率

# 打开串口
ser = serial.Serial(port, baudrate, timeout=1)  # 设置适当的超时时间

# 打开或创建一个二进制文件用于写入数据
with open('patern3.bin', 'wb') as bin_file:
    total_bytes = 128 * 1024 * 1024  # 128MB
    received_bytes = 0

    try:
        while received_bytes < total_bytes:
            # 每次读取一定数量的数据（例如，1024字节）
            data = ser.read(10*1024)

            # 检查实际读取的数据长度
            if data:
                # 将数据写入二进制文件
                bin_file.write(data)

                # 更新已接收的字节数
                received_bytes += len(data)

                # 可选：打印进度
                print(f"已接收: {received_bytes / (1024 * 1024):.2f} MB", end='\r')

    except KeyboardInterrupt:
        # 捕获Ctrl+C以安全关闭程序
        print("停止读取数据。")
    finally:
        # 关闭串口
        ser.close()

print("数据读取完成。")
