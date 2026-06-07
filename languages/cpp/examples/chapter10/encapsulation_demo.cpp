#include <iostream>

class BankAccount {
    double balance;

public:
    BankAccount() : balance(0) {}

    void deposit(double amount) {
        if (amount > 0) balance += amount;
    }

    double getBalance() const { return balance; }
};

int main() {
    BankAccount acc;
    acc.deposit(100);
    acc.deposit(50);
    std::cout << "余额：" << acc.getBalance() << std::endl;
    return 0;
}
