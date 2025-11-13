#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int id;
    char name[100];
    int qty;
    double price;
} Product;

int main(void) {
    int n = 0, extra = 0, total = 0;

    printf("Enter number of products: ");
    if (scanf("%d", &n) != 1 || n < 0) {
        fprintf(stderr, "Invalid input.\n");
        return 1;
    }

    Product *products = NULL;
    if (n > 0) {
        products = (Product *)malloc((size_t)n * sizeof(Product));
        if (!products) {
            fprintf(stderr, "Memory allocation failed.\n");
            return 1;
        }
    }

    for (int i = 0; i < n; i++) {
        printf("Product %d (ID Name Quantity Price): ", i + 1);
        if (scanf("%d %99s %d %lf",
                  &products[i].id,
                  products[i].name,
                  &products[i].qty,
                  &products[i].price) != 4) {
            fprintf(stderr, "Invalid product input.\n");
            free(products);
            return 1;
        }
    }

    printf("How many more products to add? ");
    if (scanf("%d", &extra) != 1 || extra < 0) {
        fprintf(stderr, "Invalid input.\n");
        free(products);
        return 1;
    }

    if (extra > 0) {
        Product *tmp = (Product *)realloc(products, (size_t)(n + extra) * sizeof(Product));
        if (!tmp) {
            fprintf(stderr, "Memory reallocation failed.\n");
            free(products);
            return 1;
        }
        products = tmp;

        for (int i = 0; i < extra; i++) {
            printf("Additional product %d: ", n + i + 1);
            if (scanf("%d %99s %d %lf",
                      &products[n + i].id,
                      products[n + i].name,
                      &products[n + i].qty,
                      &products[n + i].price) != 4) {
                fprintf(stderr, "Invalid product input.\n");
                free(products);
                return 1;
            }
        }
    }

    total = n + extra;

    printf("Inventory Details:\n");
    for (int i = 0; i < total; i++) {
        printf("ID: %d, Name: %s, Qty: %d, Price: $%.2f\n",
               products[i].id, products[i].name, products[i].qty, products[i].price);
    }

    free(products);
    return 0;
}