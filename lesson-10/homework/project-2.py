<<<<<<< HEAD

class Post:
    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    list_of_posts = []

    def add_post(self):
        title = input('   Title of post : ')
        content = input('   Content of post :')
        author = input('   Author of post : ')
        print()

        new_post = Post(title,content,author)
        self.list_of_posts.append(new_post)


    def list_posts(self):
        if len(self.list_of_posts) == 0:
            print('❗You don\'t have posts yet!')
            return


        print('All Blog Posts:')
        for index, i in enumerate(self.list_of_posts, start=1):
            print(f'   {index}.',i.title)
        print()

        n = int(input('Which one do you want to read: '))
        print()

        post = self.list_of_posts[n-1]
        print('Title:', post.title)
        print('Author:', post.author)
        print('Content:', post.content)
        print()


    def display_post_by_author(self):
        if len(self.list_of_posts) == 0:
            print('❗You don\'t have posts yet!')
            return

        s = set()
        for i in self.list_of_posts:
            s.add(i.author)
        l = list(s)

        print('All Authors of Blog Posts:')
        for index, i in enumerate(l,start=1):
            print(f'   {index}.',i)
        print()

        n = int(input('Choose an author: '))
        print()

        name = l[n-1]

        print(f'All Posts of {name}:')
        print()
        for i in self.list_of_posts:
            if name == i.author:
                print('Title:', i.title)
                print('Author:', i.author)
                print('Content:', i.content)
                print("-------")
                print()










def posts_menu():
    print('--------------------------------')
    print('Blog post menu:')
    print('1. Add posts')
    print('2. List all posts')
    print('3. Display posts by a specific author')
    # print('4. ')
    # print('5. ')
    print()



my_blog = Blog()

while True:
    menu = posts_menu() 
    command = input('Please eter a command: ')
    print()

    if command == '1':
        my_blog.add_post()
    elif command == '2':
        my_blog.list_posts()
    elif command == '3':
        my_blog.display_post_by_author()
    else:
=======

class Post:
    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    list_of_posts = []

    def add_post(self):
        title = input('   Title of post : ')
        content = input('   Content of post :')
        author = input('   Author of post : ')
        print()

        new_post = Post(title,content,author)
        self.list_of_posts.append(new_post)


    def list_posts(self):
        if len(self.list_of_posts) == 0:
            print('❗You don\'t have posts yet!')
            return


        print('All Blog Posts:')
        for index, i in enumerate(self.list_of_posts, start=1):
            print(f'   {index}.',i.title)
        print()

        n = int(input('Which one do you want to read: '))
        print()

        post = self.list_of_posts[n-1]
        print('Title:', post.title)
        print('Author:', post.author)
        print('Content:', post.content)
        print()


    def display_post_by_author(self):
        if len(self.list_of_posts) == 0:
            print('❗You don\'t have posts yet!')
            return

        s = set()
        for i in self.list_of_posts:
            s.add(i.author)
        l = list(s)

        print('All Authors of Blog Posts:')
        for index, i in enumerate(l,start=1):
            print(f'   {index}.',i)
        print()

        n = int(input('Choose an author: '))
        print()

        name = l[n-1]

        print(f'All Posts of {name}:')
        print()
        for i in self.list_of_posts:
            if name == i.author:
                print('Title:', i.title)
                print('Author:', i.author)
                print('Content:', i.content)
                print("-------")
                print()










def posts_menu():
    print('--------------------------------')
    print('Blog post menu:')
    print('1. Add posts')
    print('2. List all posts')
    print('3. Display posts by a specific author')
    # print('4. ')
    # print('5. ')
    print()



my_blog = Blog()

while True:
    menu = posts_menu() 
    command = input('Please eter a command: ')
    print()

    if command == '1':
        my_blog.add_post()
    elif command == '2':
        my_blog.list_posts()
    elif command == '3':
        my_blog.display_post_by_author()
    else:
>>>>>>> cf8d6416b90c8d8e28c2db3a2b57789798afffb2
        break