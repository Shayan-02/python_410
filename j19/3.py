import tkinter as tk


class ATM:
    def __init__(self, username, card_number, password, second_password, balance=0):
        """
        سازنده کلاس ATM برای تنظیم اطلاعات کاربر شامل نام کاربری، شماره کارت، رمز اول و رمز دوم و موجودی.

        :param username: نام کاربری کاربر
        :param card_number: شماره کارت کاربر
        :param password: رمز اول کاربر
        :param second_password: رمز دوم کاربر
        :param balance: موجودی حساب کاربر
        """
        self.username = username
        self.card_number = card_number
        self.password = password
        self.second_password = second_password
        self.balance = balance

    def atm_interface(self):
        """
        این تابع رابط گرافیکی برای ATM را نمایش می‌دهد و اجازه می‌دهد تا کاربر
        با وارد کردن اطلاعات خود به منوی اصلی دسترسی پیدا کند.
        """

        def validate_login():
            """
            این تابع اطلاعات وارد شده توسط کاربر را بررسی می‌کند
            و در صورت صحیح بودن وارد منوی اصلی می‌شود.
            """
            user_input = username_input.get()
            card_input = card_input_box.get()
            password_input = password_input_box.get()

            if (
                user_input == self.username
                and card_input == self.card_number
                and password_input == self.password
            ):
                status_label.config(text="Welcome!")
                display_menu()
            else:
                status_label.config(text="Invalid credentials. Please try again.")

        def display_menu():
            """
            این تابع منوی اصلی را نمایش می‌دهد و دسترسی به عملیات مختلف مانند
            واریز، برداشت، نمایش موجودی و تغییر رمزها را فراهم می‌کند.
            """
            login_frame.pack_forget()
            menu_frame.pack()

        def handle_menu_choice():
            """
            این تابع گزینه انتخابی کاربر از منو را پردازش می‌کند و عملیات مربوطه را انجام می‌دهد.
            """
            try:
                choice = int(menu_choice_entry.get())
            except ValueError:
                status_label.config(text="Please enter a valid number.")
                return

            if choice == 0:  # خروج
                status_label.config(text="Exiting...")
                root.destroy()

            elif choice == 1:  # واریز وجه
                try:
                    deposit_amount = int(amount_entry.get())
                    self.balance += deposit_amount
                    status_label.config(text=f"Deposited {deposit_amount} units.")
                except ValueError:
                    status_label.config(text="Invalid amount entered.")

            elif choice == 2:  # برداشت وجه
                try:
                    withdraw_amount = int(amount_entry.get())
                    if withdraw_amount <= self.balance:
                        self.balance -= withdraw_amount
                        status_label.config(text=f"Withdrew {withdraw_amount} units.")
                    else:
                        status_label.config(text="Insufficient balance.")
                except ValueError:
                    status_label.config(text="Invalid amount entered.")

            elif choice == 3:  # نمایش موجودی
                status_label.config(text=f"Current Balance: {self.balance}")

            elif choice == 4:  # تغییر رمز اول
                new_password = password_input_box.get()
                self.password = new_password
                status_label.config(text="Password successfully changed.")

            elif choice == 5:  # تغییر رمز دوم
                new_second_password = second_password_input_box.get()
                self.second_password = new_second_password
                status_label.config(text="Second password successfully changed.")

            else:
                status_label.config(text="Invalid choice. Please try again.")

        # ایجاد پنجره اصلی
        root = tk.Tk()
        root.title("ATM Simulator")
        root.configure(bg="#D9EAD3")  # تغییر رنگ پس‌زمینه به سبز پاستلی

        # فریم ورود
        login_frame = tk.Frame(root, bg="#D9EAD3")
        login_frame.pack()

        # لیبل‌های ورود
        username_label = tk.Label(login_frame, text="Username", bg="#D9EAD3")
        username_label.grid(row=0, column=0, padx=10, pady=5)

        card_label = tk.Label(login_frame, text="Card Number", bg="#D9EAD3")
        card_label.grid(row=1, column=0, padx=10, pady=5)

        password_label = tk.Label(login_frame, text="Password", bg="#D9EAD3")
        password_label.grid(row=2, column=0, padx=10, pady=5)

        # ورودی‌ها
        username_input = tk.Entry(login_frame)
        username_input.grid(row=0, column=1, padx=10, pady=5)

        card_input_box = tk.Entry(login_frame)
        card_input_box.grid(row=1, column=1, padx=10, pady=5)

        password_input_box = tk.Entry(login_frame, show="*")
        password_input_box.grid(row=2, column=1, padx=10, pady=5)

        # دکمه ورود
        login_button = tk.Button(
            login_frame, text="Login", command=validate_login, bg="#A2C4C9"
        )
        login_button.grid(row=3, column=1, padx=10, pady=10)

        # لیبل وضعیت
        status_label = tk.Label(root, text="", bg="#D9EAD3")
        status_label.pack(pady=10)

        # فریم منو
        menu_frame = tk.Frame(root, bg="#D9EAD3")

        menu_label = tk.Label(
            menu_frame,
            text="Choose an option:\n1. Deposit\n2. Withdraw\n3. Show Balance\n4. Change Password\n5. Change Second Password\n0. Exit",
            bg="#D9EAD3",
        )
        menu_label.pack()

        menu_choice_entry = tk.Entry(menu_frame)
        menu_choice_entry.pack(pady=10)

        amount_entry = tk.Entry(menu_frame)
        amount_entry.pack(pady=5)

        second_password_input_box = tk.Entry(menu_frame, show="*")
        second_password_input_box.pack(pady=5)

        submit_button = tk.Button(
            menu_frame, text="Submit", command=handle_menu_choice, bg="#A2C4C9"
        )
        submit_button.pack(pady=10)

        # اجرای حلقه اصلی
        root.mainloop()

        # ورودی نام کاربری
        username_label = tk.Label(login_frame, text="Username:")
        username_label.pack()
        username_input = tk.Entry(login_frame)
        username_input.pack()

        # ورودی شماره کارت
        card_label = tk.Label(login_frame, text="Card Number:")
        card_label.pack()
        card_input_box = tk.Entry(login_frame)
        card_input_box.pack()

        # ورودی رمز عبور
        password_label = tk.Label(login_frame, text="Password:")
        password_label.pack()
        password_input_box = tk.Entry(login_frame, show="*")
        password_input_box.pack()

        # دکمه ورود
        login_button = tk.Button(login_frame, text="Login", command=validate_login)
        login_button.pack()

        # لیبل وضعیت
        status_label = tk.Label(root, text="")
        status_label.pack()

        # فریم منو
        menu_frame = tk.Frame(root)

        # انتخاب عملیات
        menu_label = tk.Label(
            menu_frame,
            text="Choose an option:\n0: Exit\n1: Deposit\n2: Withdraw\n3: Show Balance\n4: Change Password\n5: Change Second Password",
        )
        menu_label.pack()

        # ورودی انتخاب منو
        menu_choice_entry = tk.Entry(menu_frame)
        menu_choice_entry.pack()

        # ورودی مبلغ
        amount_label = tk.Label(menu_frame, text="Enter Amount (for Deposit/Withdraw):")
        amount_label.pack()
        amount_entry = tk.Entry(menu_frame)
        amount_entry.pack()

        # ورودی رمز دوم
        second_password_label = tk.Label(
            menu_frame, text="Enter new second password (optional):"
        )
        second_password_label.pack()
        second_password_input_box = tk.Entry(menu_frame, show="*")
        second_password_input_box.pack()

        # دکمه پردازش
        process_button = tk.Button(
            menu_frame, text="Process", command=handle_menu_choice
        )
        process_button.pack()

        # اجرای حلقه اصلی
        root.mainloop()


# ایجاد یک شیء از کلاس ATM
atm = ATM("shayanshahbazi", "123456789", "1234568", "password2")
atm.atm_interface()
