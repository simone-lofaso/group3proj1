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
10. Buy number of products (Allen)
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
- **Pre-condition:** <can be a list or short description> User is on the cart page and has an item or items in the cart

- **Trigger:** <can be a list or short description> The event would trigger once the "remove from cart" button is clicked

- **Primary Sequence:**
  
  1. System waits for the user to click the button
  2. User clicks "remove from cart" button on a particular item
  3. System reduces the quantity by one (going from 1 --> 0)
  4. System removes that item from the cart entirely
  5. System brings up display message: "Item removed from cart"

- **Primary Postconditions:** <can be a list or short description> The system removed the product from the cart page

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. System waits for the user to click the button
  2. User clicks "remove from cart" button on a particular item
  3. System reduces the quantity by one
  4. System decreases the quantity of the product by one
  5. The ticker decreases the value by one in the cart

4. 
