#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NAME_LEN 100
#define TYPE_LEN 32

typedef union {
    long accountNumber;
    char accountType[TYPE_LEN];
    float minBalance;
} AccountInfo;

typedef struct {
    char customerName[NAME_LEN];
    int infoType; // 1-Number, 2-Type, 3-Balance
    AccountInfo info;
} BankAccount;

static void discard_line(void) {
    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF) { /* discard */ }
}

static void read_line(char *buf, size_t size) {
    if (fgets(buf, (int)size, stdin)) {
        size_t len = strlen(buf);
        if (len && buf[len - 1] == '\n') buf[len - 1] = '\0';
    } else if (size) {
        buf[0] = '\0';
    }
}

int main(void) {
    int n;

    printf("Enter number of accounts: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        fprintf(stderr, "Invalid number of accounts.\n");
        return 1;
    }
    discard_line();

    BankAccount *accounts = (BankAccount *)malloc((size_t)n * sizeof(BankAccount));
    if (!accounts) {
        fprintf(stderr, "Memory allocation failed.\n");
        return 1;
    }

    for (int i = 0; i < n; ++i) {
        printf("Account %d - Name: ", i + 1);
        read_line(accounts[i].customerName, sizeof(accounts[i].customerName));

        printf("Info type (1-Number/2-Type/3-Balance): ");
        if (scanf("%d", &accounts[i].infoType) != 1) {
            fprintf(stderr, "Invalid info type.\n");
            free(accounts);
            return 1;
        }
        discard_line();

        switch (accounts[i].infoType) {
            case 1:
                printf("Account Number: ");
                if (scanf("%ld", &accounts[i].info.accountNumber) != 1) {
                    fprintf(stderr, "Invalid account number.\n");
                    free(accounts);
                    return 1;
                }
                discard_line();
                break;
            case 2:
                printf("Account Type: ");
                read_line(accounts[i].info.accountType, sizeof(accounts[i].info.accountType));
                break;
            case 3:
                printf("Minimum Balance: ");
                if (scanf("%f", &accounts[i].info.minBalance) != 1) {
                    fprintf(stderr, "Invalid minimum balance.\n");
                    free(accounts);
                    return 1;
                }
                discard_line();
                break;
            default:
                fprintf(stderr, "Unknown info type. Use 1, 2, or 3.\n");
                free(accounts);
                return 1;
        }
    }

    printf("Bank Account Details:\n");
    for (int i = 0; i < n; ++i) {
        printf("Customer: %s, ", accounts[i].customerName);
        switch (accounts[i].infoType) {
            case 1:
                printf("Account Number: %ld\n", accounts[i].info.accountNumber);
                break;
            case 2:
                printf("Account Type: %s\n", accounts[i].info.accountType);
                break;
            case 3:
                printf("Min Balance: $%.2f\n", accounts[i].info.minBalance);
                break;
            default:
                printf("No valid info\n");
                break;
        }
    }

    free(accounts);
    return 0;
}