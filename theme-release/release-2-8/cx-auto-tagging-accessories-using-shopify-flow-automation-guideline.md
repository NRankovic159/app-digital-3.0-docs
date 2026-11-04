# [2.8] CX_Auto-tagging Accessories Using Shopify Flow Automation Guideline

This guide provides APP partners with a step-by-step process for creating and managing an automated workflow -"Auto-tag Accessories After Data Push". This automation, built using the Shopify Flow application, streamlines the process of tagging accessory products based on specific keywords in their product information.

## 1. Purpose of the Guideline

The primary purpose of this document is to enable APP partners to independently implement and adapt a Shopify Flow automation. This workflow automatically tags newly created accessory products based on keywords in Primary Display product metafield and Product Type. By following this guide, you will be able to save time on manual product tagging, ensure consistency in your product organization, and improve the discoverability of accessories on your storefront.

Please note: adding a tag to a product so it's automatically assigned to a collection will only work if that collection is a Smart Collection. The collection must have a corresponding rule configured to include products with that specific tag.

Please also note: This guide does not cover the process of creating Smart Collections; it assumes that the relevant collections have already been set up.

## 2. Crafting the "Auto-tag Accessories" Workflow

This section will walk you through recreating the "Auto-tag Accessories After Data Push" workflow in your own Shopify store. The process involves setting up a trigger that initiates the workflow, and then adding a series of conditions and actions to tag your products automatically.

### 2.1. Prerequisites

Before you begin, ensure that you have the Shopify Flow app installed in your Shopify store. You can find and install it for free from the Shopify App Store. Aditionnaly make sure you have created accessories collections as smart collections and have correct rules that checks appropriate product tags.

### 2.2. Recreating the Workflow

Follow these instructions to build the automation:

1. **Open Shopify Flow and Create a New Workflow:**
   1. From your Shopify admin, navigate to Apps and open the Shopify Flow app.
   2. Click on the "Create workflow" button to start a new automation.
2. **Select the Trigger:**
   1. A trigger is an event that starts your workflow. For this automation, the trigger will be the creation of a new product.
   2. Click on "Select a trigger" and choose "Product created". This means the workflow will run every time a new product is added to your store.
3. **Add the Main Condition:**
   1. Click the "+" button below the trigger and select "Condition".
   2. This condition will check if the newly created product is an "Accessory."
   3. In the condition block, set the following criteria:
      1. If: Product type
      2. is equal to: Accessories
4. **Add Conditions for Keyword-Based Tagging:**
   1. Under the "Then" branch of the main condition, click the "+" button and add another "Condition". This will be a nested condition.
   2. This condition will check for specific keywords within the "Primary Display" product metafield.
   3. To set up the condition:
      1. In the "If" statement, search for and select the product metafield that corresponds to "Primary Display".
      2. Choose the "contains" operator.
      3. Enter the keyword you want to check for. For example, if you are tagging items for the "iPad accessories" you would enter iPad.
5. **Add the Tagging Action:**
   1. If the above condition is true, the next step is to add the relevant tag.
   2. Under the "Then" branch of the keyword condition, click the "+" button and select "Action".
   3. Search for and choose the "Add product tag" action.
   4. In the "Tags" field, enter the tag you want to add (e.g., iPad Accessories).
6. **Repeat for Additional Keywords and Tags:**
   1. To add more tags based on different keywords, you will add more conditions. Under the "If false" branch of the previous keyword condition, click the "+" and add a new "Condition".
   2. Repeat steps 4 and 5 for each new keyword and corresponding tag you want to automate. For instance, you could add another condition to check if the "Primary Display" metafield contains "iPhone" and, if true, add the tag iPhone Accessories.

### 2.3. Handling Accessories Without a Specific Keyword

After checking for all your specific keywords, some accessory products might not contain any of them. We can create a "catch-all" step to tag these general accessories. This is done in the final "If false" branch of your workflow.

1. **Create “catch-all" condition:** Scroll down to the very last condition you created. This point represents products that are accessories but did not match any of the keywords you checked for.
   1. Under the "Then" branch of the main condition, click the "+" button and add another "Condition"
   2. Add all previously added conditions into one condition combined with an “OR” operator
2. **Add the Final Action:**
   1. Under this final "If false" branch, click the "+" button and select "Action".
   2. Choose the "Add product tag" action.
   3. In the "Tags" field, enter all the tags that apply to your general accessories. This ensures that even if a product doesn't fit a specific collection, it is still tagged as accessorie product since it has Product Type = “Accessories”.
3. **Activate the Workflow:**
   1. Once you have added all your conditions and the final catch-all action, give your workflow a descriptive name, such as "Auto-tag Accessories After Data Push."
   2. Click "Turn on workflow" to activate it.

## 3. Extending the Shopify Flow on Demand

As your product offerings evolve, you may need to update this workflow to include new accessory types or descriptive keywords. Here’s how to extend the automation:

1. **Navigate to Your Workflow:** Open the Shopify Flow app and select the "Auto-tag Accessories After Data Push" workflow to edit it.
2. **Add a New Condition for a New Keyword:**
   1. Scroll to the last condition in your workflow.
   2. Click the "+" icon under the final "If false" branch and select "Condition".
3. **Define the New Condition:**
   1. Set the condition to check your "Primary Display" product metafield for the new keyword you want to target (e.g., Mac).
   2. Ensure the operator is set to "contains".
4. **Add the Corresponding New Tag:**
   1. Under the "Then" branch of your new condition, click the "+" icon and select "Action".
   2. Choose the "Add product tag" action.
   3. Enter the new tag that corresponds to your new keyword (e.g., Mac Accessories).
5. **Save Your Changes:** Once you've added the new condition and action, ensure you save the workflow to apply the updates.

## 4. Conclusion

This automated workflow is a powerful tool for efficiently managing your accessory products in Shopify. By automating the tagging process, you reduce the potential for human error and free up valuable time to focus on other aspects of your business. The flexibility of Shopify Flow allows you to easily adapt and expand this automation as your product catalog grows, ensuring your store remains well-organized and user-friendly.

## Additional document

{% file src="../../.gitbook/assets/Auto-tag_Accessories_After_Data_Push.flow" %}
Auto-tag_Accessories_After_Data_Push.flow
{% endfile %}
