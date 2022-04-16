## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. Login
2. Logout
3. Create New Account
4. Delete Account
5. Search
6. Add to cart
7. Remove from cart
8. View item description
9. Save payment info
10. Buy Now
11. Quantity 
12. Post item for sale
13. 13. *Add pictures for items  ------------ HP

## Non-functional Requirements

1. Round up for charity
2. Change Language? ***** Highpass
3. Light/Dark Mode?
4. Are you human? (Captcha)

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