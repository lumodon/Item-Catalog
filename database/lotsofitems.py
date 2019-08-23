#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item

if __name__ == '__main__':
    engine = create_engine('sqlite:///database/catalog.db')
    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    # A DBSession() instance establishes all conversations with the database
    # and represents a "staging zone" for all the objects loaded into the
    # database session object. Any change made against the objects in the
    # session won't be persisted into the database until you call
    # session.commit(). If you're not happy about the changes, you can
    # revert all of them back to the last commit by calling
    # session.rollback()
    session = DBSession()

    # Menu for UrbanBurger
    category1 = Category(name="Urban Burger")

    session.add(category1)
    session.commit()

    item2 = Item(name="Veggie Burger", description="Juicy grilled veggie patty"
                 "with tomato mayo and lettuce",
                 owner_id="initial_user", category=category1)

    session.add(item2)
    session.commit()
    item1 = Item(name="French Fries", description="with garlic and parmesan",
                 owner_id="initial_user", category=category1)

    session.add(item1)
    session.commit()

    item2 = Item(name="Chicken Burger", description="Juicy grilled chicken"
                 "patty with tomato mayo and lettuce",
                 owner_id="initial_user", category=category1)

    session.add(item2)
    session.commit()

    item3 = Item(name="Chocolate Cake", description="fresh baked and served"
                 " with ice cream",
                 owner_id="initial_user", category=category1)

    session.add(item3)
    session.commit()

    item4 = Item(name="Sirloin Burger", description="Made with grade A beef",
                 owner_id="initial_user", category=category1)

    session.add(item4)
    session.commit()

    item5 = Item(name="Root Beer", description="16oz of refreshing goodness",
                 owner_id="initial_user", category=category1)

    session.add(item5)
    session.commit()

    item6 = Item(name="Iced Tea", description="with Lemon",
                 owner_id="initial_user", category=category1)

    session.add(item6)
    session.commit()

    item7 = Item(name="Grilled Cheese Sandwich", description="On texas toast"
                 " with American Cheese",
                 owner_id="initial_user", category=category1)

    session.add(item7)
    session.commit()

    item8 = Item(name="Veggie Burger", description="Made with freshest of"
                 " ingredients and home grown spices",
                 owner_id="initial_user", category=category1)

    session.add(item8)
    session.commit()

    # Menu for Super Stir Fry
    category2 = Category(name="Super Stir Fry")

    session.add(category2)
    session.commit()

    item1 = Item(name="Chicken Stir Fry", description="With your choice of"
                 " noodles vegetables and sauces",
                 owner_id="initial_user", category=category2)

    session.add(item1)
    session.commit()

    item2 = Item(
        name="Peking Duck", description=" A famous duck dish from Beijing[1]"
        " that has been prepared since the imperial era. The meat is prized "
        "for its thin, crisp skin, with authentic versions of the dish "
        "serving mostly the skin and little meat, sliced in front of the "
        "diners by the cook", owner_id="initial_user", category=category2)

    session.add(item2)
    session.commit()

    item3 = Item(name="Spicy Tuna Roll", description="Seared rare ahi, "
                 "avocado, edamame, cucumber with wasabi soy sauce ",
                 owner_id="initial_user", category=category2)

    session.add(item3)
    session.commit()

    item4 = Item(name="Nepali Momo ", description="Steamed dumplings made "
                 "with vegetables, spices and meat. ",
                 owner_id="initial_user", category=category2)

    session.add(item4)
    session.commit()

    item5 = Item(name="Beef Noodle Soup", description="A Chinese noodle "
                 "soup made of stewed or red braised beef, beef broth, "
                 "vegetables and Chinese noodles.",
                 owner_id="initial_user", category=category2)

    session.add(item5)
    session.commit()

    item6 = Item(name="Ramen", description="a Japanese noodle soup dish. "
                 "It consists of Chinese-style wheat noodles served in a "
                 "meat- or (occasionally) fish-based broth, often flavored"
                 " with soy sauce or miso, and uses toppings such as sliced"
                 " pork, dried seaweed, kamaboko, and green onions.",
                 owner_id="initial_user", category=category2)

    session.add(item6)
    session.commit()

    # Menu for Panda Garden
    category1 = Category(name="Panda Garden")

    session.add(category1)
    session.commit()

    item1 = Item(name="Pho", description="a Vietnamese noodle soup consisting "
                 "of broth, linguine-shaped rice noodles called banh pho,"
                 " a few herbs, and meat.",
                 owner_id="initial_user", category=category1)

    session.add(item1)
    session.commit()

    item2 = Item(name="Chinese Dumplings", description="a common Chinese "
                 "dumpling which generally consists of minced meat and finely"
                 " chopped vegetables wrapped into a piece of dough skin. "
                 "The skin can be either thin and elastic or thicker.",
                 owner_id="initial_user", category=category1)

    session.add(item2)
    session.commit()

    item3 = Item(name="Gyoza", description="The most prominent differences "
                 "between Japanese-style gyoza and Chinese-style jiaozi are"
                 " the rich garlic flavor, which is less noticeable in the "
                 "Chinese version, the light seasoning of Japanese gyoza "
                 "with salt and soy sauce, and the fact that gyoza wrappers"
                 " are much thinner", owner_id="initial_user",
                 category=category1)

    session.add(item3)
    session.commit()

    item4 = Item(name="Stinky Tofu", description="Taiwanese dish, deep fried"
                 " fermented tofu served with pickled cabbage.",
                 owner_id="initial_user", category=category1)

    session.add(item4)
    session.commit()

    item2 = Item(name="Veggie Burger", description="Juicy grilled veggie "
                 "patty with tomato mayo and lettuce",
                 owner_id="initial_user", category=category1)

    session.add(item2)
    session.commit()

    # Menu for Thyme for that
    category1 = Category(name="Thyme for That Vegetarian Cuisine ")

    session.add(category1)
    session.commit()

    item1 = Item(name="Tres Leches Cake", description="Rich, luscious sponge"
                 " cake soaked in sweet milk and topped with vanilla bean "
                 "whipped cream and strawberries.",
                 owner_id="initial_user", category=category1)

    session.add(item1)
    session.commit()

    item2 = Item(name="Mushroom risotto", description="Portabello mushrooms "
                 "in a creamy risotto", owner_id="initial_user",
                 category=category1)

    session.add(item2)
    session.commit()

    item3 = Item(name="Honey Boba Shaved Snow", description="Milk snow "
                 "layered with honey boba, jasmine tea jelly, grass jelly,"
                 " caramel, cream, and freshly made mochi",
                 owner_id="initial_user", category=category1)

    session.add(item3)
    session.commit()

    item4 = Item(name="Cauliflower Manchurian", description="Golden fried "
                 "cauliflower florets in a midly spiced soya,garlic sauce "
                 "cooked with fresh cilantro, celery, chilies,ginger & "
                 "green onions", owner_id="initial_user", category=category1)

    session.add(item4)
    session.commit()

    item5 = Item(name="Aloo Gobi Burrito", description="Vegan goodness. "
                 "Burrito filled with rice, garbanzo beans, curry sauce, "
                 "potatoes (aloo), fried cauliflower (gobi) and chutney. "
                 "Nom Nom", owner_id="initial_user", category=category1)

    session.add(item5)
    session.commit()

    item2 = Item(name="Veggie Burger", description="Juicy grilled veggie "
                 "patty with tomato mayo and lettuce", owner_id="initial_user",
                 category=category1)

    session.add(item2)
    session.commit()

    # Menu for Tony's Bistro
    category1 = Category(name="Tony\'s Bistro ")

    session.add(category1)
    session.commit()

    item1 = Item(name="Shellfish Tower", description="Lobster, shrimp, sea"
                 "snails, crawfish, stacked into a delicious tower",
                 owner_id="initial_user", category=category1)

    session.add(item1)
    session.commit()

    item2 = Item(name="Chicken and Rice", description="Chicken... and rice",
                 owner_id="initial_user", category=category1)

    session.add(item2)
    session.commit()

    item3 = Item(name="Mom's Spaghetti", description="Spaghetti with some "
                 "incredible tomato sauce made by mom",
                 owner_id="initial_user", category=category1)

    session.add(item3)
    session.commit()

    item4 = Item(name="Choc Full O\' Mint (Smitten\'s Fresh Mint "
                 "Chip ice cream)",
                 description="Milk, cream, salt, ..., Liquid nitrogen magic",
                 owner_id="initial_user", category=category1)

    session.add(item4)
    session.commit()

    item5 = Item(name="Tonkatsu Ramen", description="Noodles in a delicious "
                 "pork-based broth with a soft-boiled egg",
                 owner_id="initial_user", category=category1)

    session.add(item5)
    session.commit()

    # Menu for Andala's
    category1 = Category(name="Andala\'s")

    session.add(category1)
    session.commit()

    item1 = Item(name="Lamb Curry", description="Slow cook that thang in a "
                 "pool of tomatoes, onions and alllll those tasty Indian"
                 " spices. Mmmm.", owner_id="initial_user", category=category1)

    session.add(item1)
    session.commit()

    item2 = Item(name="Chicken Marsala", description="Chicken cooked in "
                 "Marsala wine sauce with mushrooms",
                 owner_id="initial_user", category=category1)

    session.add(item2)
    session.commit()

    item3 = Item(name="Potstickers", description="Delicious chicken and "
                 "veggies encapsulated in fried dough.",
                 owner_id="initial_user", category=category1)

    session.add(item3)
    session.commit()

    item4 = Item(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, "
                 "Unagi, Uni, TORO!",
                 owner_id="initial_user", category=category1)

    session.add(item4)
    session.commit()

    item2 = Item(name="Veggie Burger", description="Juicy grilled veggie patty"
                 " with tomato mayo and lettuce",
                 owner_id="initial_user", category=category1)

    session.add(item2)
    session.commit()

    # Menu for Auntie Ann's
    category1 = Category(name="Auntie Ann\'s Diner' ")

    session.add(category1)
    session.commit()

    item9 = Item(name="Chicken Fried Steak", description="Fresh battered "
                 "sirloin steak fried and smothered with cream gravy",
                 owner_id="initial_user", category=category1)

    session.add(item9)
    session.commit()

    item1 = Item(name="Boysenberry Sorbet", description="An unsettlingly "
                 "huge amount of ripe berries turned into frozen "
                 "(and seedless) awesomeness", owner_id="initial_user",
                 category=category1)

    session.add(item1)
    session.commit()

    item2 = Item(name="Broiled salmon", description="Salmon fillet "
                 "marinated with fresh herbs and broiled hot & fast",
                 owner_id="initial_user", category=category1)

    session.add(item2)
    session.commit()

    item3 = Item(name="Morels on toast (seasonal)", description="Wild morel "
                 "mushrooms fried in butter, served on herbed toast slices",
                 owner_id="initial_user", category=category1)

    session.add(item3)
    session.commit()

    item4 = Item(name="Tandoori Chicken", description="Chicken marinated "
                 "in yoghurt and seasoned with a spicy mix(chilli, tamarind "
                 "among others) and slow cooked in a cylindrical clay or "
                 "metal oven which gets its heat from burning charcoal.",
                 owner_id="initial_user", category=category1)

    session.add(item4)
    session.commit()

    item2 = Item(name="Veggie Burger", description="Juicy grilled veggie "
                 "patty with tomato mayo and lettuce",
                 owner_id="initial_user", category=category1)

    session.add(item2)
    session.commit()

    item10 = Item(name="Spinach Ice Cream", description="vanilla ice cream "
                  "made with organic spinach leaves",
                  owner_id="initial_user", category=category1)

    session.add(item10)
    session.commit()

    # Menu for Cocina Y Amor
    category1 = Category(name="Cocina Y Amor ")

    session.add(category1)
    session.commit()

    item1 = Item(name="Super Burrito Al Pastor", description="Marinated Pork, "
                 "Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                 owner_id="initial_user", category=category1)

    session.add(item1)
    session.commit()

    item2 = Item(name="Cachapa", description="Golden brown, corn-based "
                 "Venezuelan pancake; usually stuffed with queso telita or "
                 "queso de mano, and possibly lechon. ",
                 owner_id="initial_user", category=category1)

    session.add(item2)
    session.commit()

    category1 = Category(name="State Bird Provisions")
    session.add(category1)
    session.commit()

    item1 = Item(name="Chantrelle Toast", description="Crispy Toast with "
                 "Sesame Seeds slathered with buttery chantrelle mushrooms",
                 owner_id="initial_user", category=category1)

    session.add(item1)
    session.commit

    item1 = Item(name="Guanciale Chawanmushi", description="Japanese egg "
                 "custard served hot with spicey Italian Pork Jowl "
                 "(guanciale)", owner_id="initial_user", category=category1)

    session.add(item1)
    session.commit()

    item1 = Item(name="Lemon Curd Ice Cream Sandwich", description="Lemon "
                 "Curd Ice Cream Sandwich on a chocolate macaron with "
                 "cardamom meringue and cashews", owner_id="initial_user",
                 category=category1)

    session.add(item1)
    session.commit()

    print "added menu items!"
