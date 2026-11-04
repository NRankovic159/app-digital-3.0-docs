# Checkout Header Cart Link & BOPIS Reorder Installation Guideline

## 1. Purpose of the Guideline

This guideline outlines how to add a newly created cart link to the Checkout page header.

## 2. Add Checkout Cart Link

### 2.1 Prerequisites

Please ensure you have updated the application and verify that a new "checkout-cart-link-ui" folder is now present within the "extensions" directory.

### 2.2 Add Cart link via Customizer

1. Open Settings – Checkout and click the “Customize” button next to the live checkout profile.
2. In the Header section click on the “Add block” button. In a new modal window, click on the “checkout-cart-link-ui” block.
3. Save changes.

## 3. BOPIS Reorder Function Installation

### 3.1 Prerequsites

Please ensure you have updated the application and verify that a new " bopis-reorder-preselected-location " folder is now present within the "extensions" directory and you have published Theme version 2.8 or higher.

### 3.2 BOPIS Reorder Function Registration

Open the Shopify GraphQL application and run getFunctionId query by pasting the following code:

```graphql
query getFunctionId {
    shopifyFunctions(first: 50) {
        edges {
            node {
                id
                title
            }
        }
    }
}
```

In the response window find function with the name “bopis-location-reorder” and copy its ID:

Create a new request by pasting the following graphql code:

```graphql
mutation deliveryCustomizationCreate($functionId: String!, $title: String!) {
    deliveryCustomizationCreate(
        deliveryCustomization: {
            functionId: $functionId
            title: $title
            enabled: true
        }
    ){
        deliveryCustomization {
            id
        }
        userErrors {
            field
            message
        }
    }
}
```

Paste the following variables in the “Variables” section for the deliveryCustomizationCreate mutation query. Change functionId with the ID from the first request:

```json
{
    "functionId": "your_bopis_location_reorder_function_id",
    "title": "Reorder Delivery by Location"
}
```
