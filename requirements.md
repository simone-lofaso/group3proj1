## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. Login (Yashik)
2. Logout (Yashik) 
3. Create New Account (Yashik)
4. Delete Account (Yashik)
5. Search (Simone)
6. Add to cart (Simone)
7. Remove from cart (Simone)
8. View item description (Simone)
9. Save payment info (Allen)
10. Buy product (Allen)
11. Post item for sale (Allen)
12. *Add pictures for items (Allen)

## Non-functional Requirements

1. Round up for charity (Saim)
2. Change Language? (Saim)
3. Light/Dark Mode? (Saim)
4. Captcha (Saim)

## Use Cases

1. Search 
- **Pre-condition:** <can be a list or short description> The textbox contains text that is a String with information that could or could not be on the website

- **Trigger:** <can be a list or short description> The event would trigger once the enter button is clicked or when the search button is clicked

- **Primary Sequence:**
  
  1. System asks the user for text to enter in the search box
  2. User types in the text in the search box
  3. User hits enter or clicks the search button
  4. System checks with its list of products to see what brings up a match
  5. System brings up a filtered list of products to the user
  6. User looks for products that have narrowed down his search using the key words in the search box

- **Primary Postconditions:** <can be a list or short description> The user has a filtered product list who is searching with the hope to find a product that they searched for

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. System asks the user for text to enter in the search box
  2. User types in the text in the search box
  3. User hits enter or clicks the search button
  4. System check with its list of products but can't find any matches
  5. System displays "No Matches Found"
  6. User either changes text in search box (repeat sequence) or leaves website

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. System asks user for text to enter in the search box
  2. User types nothing into the search box
  3. User hits enter or clicks on the search button
  4. System can't find any matches with an empty string
  5. System filters the products to none (no products)
  6. System displays "No Matches Found"
  7. User either changes text in search box (repeat sequence) or leaves website

2. Add to cart
- **Pre-condition:** <can be a list or short description> User is on the product page and clicks on the "add to cart" button

- **Trigger:** <can be a list or short description> The event would trigger once the "add to cart" button is clicked 

- **Primary Sequence:**
  
  1. System waits for the user to click the button
  2. User clicks button
  3. System checks if product is found in database
  4. System adds the product to the cart (with or without other products)
  5. System brings up display message: "Item added to cart"

- **Primary Postconditions:** <can be a list or short description> The system added the product the user requested into the cart without any problems

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. System waits for the user to click the button
  2. User increments the quanitity from one to another number
  3. User clicks button
  4. System checks if product is found in database
  5. System adds the multiple copies of the product to the cart (with or without other products)
  6. User either changes text in search box (repeat sequence) or leaves website


3. Remove from Cart
- **Pre-condition:** User is on the cart page and has an item or items in the cart

- **Trigger:** The event would trigger once the "remove from cart" button is clicked

- **Primary Sequence:**
  
  1. System waits for the user to click the button
  2. User clicks "remove from cart" button on a particular item
  3. System reduces the quantity by one (going from 1 --> 0)
  4. System removes that item from the cart entirely
  5. System brings up display message: "Item removed from cart"

- **Primary Postconditions:** The system removed the product from the cart page

- **Alternate Sequence:**
  
  1. System waits for the user to click the button
  2. User clicks "remove from cart" button on a particular item
  3. System reduces the quantity by one
  4. System decreases the quantity of the product by one
  5. The ticker decreases the value by one in the cart

4. View Item Description 
- **Pre-condition:** User has to have used the search function to display items of interest

- **Trigger:** The event would trigger when the image or name of the item has been clicked

- **Primary Sequence:** 
  1. System waits for the user to click the the image or name of the product
  2. User clicks the name or image of the product
  3. The system redirects the user to another page
  4. The page will then show the image of the product, price, and description. Other functions such as buy now and add to cart
     will also be displayed

- **Primary Postconditions:** The page of the product will be displayed for the user to see and buy

 **Alternate Sequence:**

  1. System waits for the user to click the the image or name of the product
  2. User clicks the name or image of the product
  3. The system will redirect the user to anoter page
  4. The page will display; product not found

5. Save Payment
- **Pre-condition:** The user needs to be logged in and needs to have selected the save payment option through the account settings, or 
  the option can be first done in the create account section.

- **Trigger:** The save payment option has to be clicked

- **Primary Sequence:**

  1. The system waits for the user to click the save payment button
  2. The user clicks the save payment button
  3. The user will be redirected to another page
  4. The page will display text boxes to fill in your card information
  5. The user will enter their card information and click save when all boxes are filled
  6. The system will check with the bank if the card is valid
  7. The bank will approve the card
  8. The system will transfer the card information into their database which will be connected to the account

- **Primary Postconditions:** The account will be linked to their card information and can buy items

- **Alternate Sequence:**

  1. The system waits for the user to click the save payment button
  2. The user clicks the save payment button
  3. The user will be redirected to another page
  4. The page will display text boxes to fill in your card information 
  5. The user will enter their card information and click save when all boxes are filled
  6. The system will check with the bank if the card is valid
  7. The card is not valid or is missing information
  8. The bank will not approve of the card
  9. The system will tell the user to re-enter their card information

6. Buy product
- **Pre-condition:** Must be in the cart page and is logged in

- **Trigger:** The 'Buy' button must be clicked in the cart page

- **Primary Sequence:**

  1. The system waits for the user to click the buy button in the cart page
  2. The user clicks the buy button
  3. The system redirects user to another page
  4. The page will contain their card information that they have saved and text boxes for the shipping address
  5. After checking card information and filling out the shipping address they will click the proceed to checkout button
  6. The user will be redirected to a page that will list all the details pertaining card information, shipping address, costs, number of products, ect
  7. After reviewing this page, the user will click the 'order' button
  8. The system will process this order by sending this information (excluding card) to the seller.

- **Primary Postconditions:** The user will have purchased the items in the cart and the seller will have the user's information

- **Alternate Sequence:**

  1. The system waits for the user to click the buy button in the cart page
  2. The user clicks the buy button
  3. The system recognizes that their is no card information tied with this account in the database
  4. The system will then redirect the user to the save payment page

