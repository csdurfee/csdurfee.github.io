Title: Laravel's weird models
Date: 2026-06-07 10:20
Category: software development
Tags: security, Laravel

[![Herbie Hancock and Wah Wah Watson, "Hang Up Your Hang Ups"](https://img.youtube.com/vi/K3lgmnsTdcA/0.jpg)](https://www.youtube.com/watch?v=K3lgmnsTdcA){:target="_blank"}

Song: [Herbie Hancock and Wah Wah Watson, "Hang Up Your Hang Ups"](https://www.youtube.com/watch?v=K3lgmnsTdcA){:target="_blank"}

Like I said last week, I think Laravel's a good framework. It's really easy to get started while being sophisticated enough to handle complex use cases, it has some genuinely good ideas, and a vibrant community supporting it. Overall, I would recommend it despite its flaws. But it's more interesting to talk about a system that mostly does things well than something that's crap.

In the [traditional definition of Model-View-Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller), which dates back to the 1970's, models should be the biggest and most important part of the system. The controller and the view should both be fairly minimal layers that support the model.

In the typical MVC web framework, models usually aren't as central as in the traditional definition, but they should give a good picture of the actual data used by the system -- how it's organized, how it relates to other data, what the data types are, what the validation rules are. Laravel's models do hardly any of that. 

Here's the SQL schema for the default Laravel `user` table:

```sql
CREATE TABLE IF NOT EXISTS "users" (
    "id" integer primary key autoincrement not null, 
    "name" varchar not null, 
    "email" varchar not null,
    "email_verified_at" datetime, 
    "password" varchar not null, 
    "remember_token" varchar, 
    "created_at" datetime, 
    "updated_at" datetime
);
```

Here's the corresponding Laravel model:

```php
<?php 

#[Fillable(['name', 'email', 'password'])]
#[Hidden(['password', 'remember_token'])]
class User extends Authenticatable
{
    /** @use HasFactory<UserFactory> */
    use HasFactory, Notifiable;

    /**
     * Get the attributes that should be cast.
     *
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'email_verified_at' => 'datetime',
            'password' => 'hashed',
        ];
    }
}
?>
```

The model tells us almost nothing about what a user record is or how it works. It doesn't tell us which properties exist and what their datatypes are. If you know what "Fillable" means to Laravel, you can tell that the user should be allowed to mass-update the name, email and password fields, but the rest of it is pretty useless as documentation of how the model actually works.

You might notice `created_at` and `updated_at` are also datetime fields in the SQL, like `email_verified_at`. So why don't those properties need to be cast as well? Laravel tries to add those columns to *every.single.table* in the database unless you explicitly turn it off, and they are handled *automagically*. (Find someone who loves you as much as Laravel loves those auto-added timestamps.) 

Why not have the actual functions doing the casting referenced in the model rather than strings? PHP has first class functions; we don't need to use strings as the values in the array returned by `casts()`. I shouldn't really have to know what function `hashed` or `datetime` maps to, I should just be able to click on the function name to get to the definition.

Neither the SQL nor the model class tell us if any validation is being done on the data, or where. Databases *can* do data validation using `CHECK` constraints, so in a more old-fashioned type of database, we might get that info from the SQL schema. It would be nice if ORMs set up `CHECK` constraints as a part of the table schema, but I've never seen one that does. It's a shame, because there's a pretty suprising bug here because I'm using SQLite for the dtabase. SQLite varchar fields are text fields by another name, which can be up to a billion characters long. You can specify a `VARCHAR(100)` or whatever, but the database doesn't enforce it. If we want to restrict a SQLite text field to always be some reasonable length, we *have* to use `CHECK` constraints.

Do we really want to allow billion character long usernames (*tres commas*!), or is there something in the PHP code that limits their length? Can we trust that code always getss run?  Name, email and password are `not null` in the DB. Is something checking to see that's true before trying to write to the database, or is it relying on the database server to return an error if those columns are omitted? Shouldn't usernames and/or email addresses be unique? How is that enforced?

These are pretty reasonable questions to ask, and most MVC frameworks will give you the answers just by looking at the model classes.  To answer those questions in Laravel, you have to look at everywhere in the code it writes to the database, and what bespoke set of validations are being used in each place. There's no reason to believe validation is being applied in a uniform fashion.

For contrast, here's what part of a [Django](https://www.djangoproject.com/) user model looks like:

```python
class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True)    
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    password = models.CharField(_("password"), max_length=128)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
```

We can immediately tell what data types the fields are, which ones are required, and what validation is run on each field. The `username_validator` is supplied as the actual function, not some string that gets mapped to a function somewhere in the depths of the framework, so you can just click on it and be taken to the definition.

We can get to the definition of `EmailField` in one click in an IDE, and see that it tries to validate the email address against the official RFC. We can also see that the labels and error messages will be internationalized by the `_()` function. Nice.

Most of all, we can feel confident that these validators and constraints will be applied anywhere in the code that is using the User class. The validations are correctly encapsulated in the model.

PHP isn't capable of as much Fancy Metaprogramming Magic as Python/Ruby, so the syntax can't be as elegant as Django's, but why can't we just declare the columns in the model class in Laravel? For instance, could we have a `public string $username` property on the class that the ORM fills in? [That's how Yii works](https://www.yiiframework.com/doc/guide/2.0/en/structure-models#attributes). [Symfony, too](https://symfony.com/doc/current/doctrine.html). It at least gives some sense of what the columns are on the database and how they map to PHP types, and it makes code completion work in the IDE.

Unfortunately, if you try that in Laravel, you'll error about `Typed property $name must not be accessed before initialization`. You can't actually define the model in your model classes, because it interferes with Laravel's use of [PHP's `__get()` and `__call()` *magic* methods](https://www.php.net/manual/en/language.oop5.magic.php).

There's a 3rd party library called [Laravel Lift](https://wendell-adriel.gitbook.io/laravel-lift) that makes it possible to write saner Laravel models, through heavy use of PHP attributes and Laravel events. For example, we could use Lift's `Config` attribute to attach behavior to a string typed `$username` field. The attribute below will allow `$username` to be set through mass-assignment, requires it not be blank, and provides the error message if it is blank. That gets us pretty close to what Django models do.

```php
<?php
use WendellAdriel\Lift\Attributes\Config;
//...
class User {
    use Lift;

    #[Config(fillable: true, 
            rules: ['required', 'string'], 
            messages: ['required' => 'The name field cannot be empty.'])]
    public string $username;
//...
}
```

As Lift's namespace clearly indicates, it's Just Some Wendell's experiment. But it's a pretty compelling proof of concept, at the very least -- whether you want to trust it in production or not is your call. The package has been around for three years, so there's some longevity. But it's puzzling that similar functionality isn't a core part of Laravel by now. 

There are a half dozen ways of doing every trivial thing in Laravel, but not even one way to do this super important thing? Along with the lack of Role-Based Access Control, it makes me wonder if the people setting the direction for Laravel know what really matters in the real world.

It's weird because Laravel, like everybody, is chasing the AI zeitgeist at this point. Type hinting is kind of having a moment these days, because it makes AI and humans using them better at making reliable stuff quickly. Isn't that more important than all the crap in Laravel's [official AI SDK](https://laravel.com/docs/13.x/ai-sdk#images) that I have a hard time imagining anybody using?

### Searching for a source of truth
If you can't declare the columns in the model file, where do you declare them in Laravel? The closest thing to a source of truth ends up being the migrations used to create/modify the tables used. Here's the migration to create the user table:

```php
<?php

Schema::create('users', function (Blueprint $table) {
        $table->id();
        $table->string('name');
        $table->string('email')->unique();
        $table->timestamp('email_verified_at')->nullable();
        $table->string('password');
        $table->rememberToken();
        $table->timestamps();
    });
```

That still doesn't give us the whole picture, though. For instance, there may be later migrations that alter the table by adding more columns, or changing the datatypes. The `$table->timestamps()` call is what adds both the `created_at` and `updated_at` columns to the database. So there isn't even a 1:1 correspondence between this file and the database schema produced.

It seems almost too obvious to say, but model classes should encapsulate the logic around how the model works. That's what they're there for. [Cohesion is good](https://en.wikipedia.org/wiki/Cohesion_%28computer_science%29). The whole point of MVC frameworks (and design patterns in general) is to split a complex problem into components that serve familiar roles and interact in predictable ways. Laravel does a good job of that a lot of the time, but this ain't it. 

### Validations: the other side of security
Validation rules are critical for ensuring that the data in the database is in a standard, predictable format. Validation isn't a separate concern from what the model does. It's integral to it. Weird data in the database always always always leads to weird bugs downstream. For more benign bugs, either somebody goes in and cleans the data up, or everybody has to remember that sometimes the `foo` field is a null and sometimes it's a blank string, and code around it till the end of time.

Lack of validation can lead to security issues as well -- XSS, SQL Injection, and Remote Code Execution can all start with bad validation/sanitization/type checking on data written to the database. Like authorization, it's deceptively hard to do validation right, and kinda boring, but extremely important.

So how does Laravel do validation? If you read the last post, it shouldn't surprise you to learn that there are a bunch of options, and [the documentation](https://laravel.com/docs/13.x/validation) tells you to use whatever you feel like.

The first recommended method is to do validation in the controller class where the data is being submitted to. An example directly from the documentation:

```php
<?php

public function store(Request $request): RedirectResponse
{
    $validated = $request->validate([
        'title' => ['required', 'unique:posts', 'max:255'],
        'body' => ['required'],
    ]);
 
    // The blog post is valid...
 
    return redirect('/posts');
}
```

That means the validation is being done on the HTTP request, which is an obvious separation of concerns issue. The controller *should* be doing validation, but not this kind. Type checking on the request parameters before any model-related code is run is a good way to build [defense in depth](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)). I wish HTTP request level type checking was baked into more MVC frameworks. I've used it before to improve security across the board on a huge *legacy* MVC app. It was well worth the effort to add security checks to the request object itself, eliminating hundreds of potential XSS vectors at one go.

If the `page=` parameter isn't an integer but an attempt at XSS or SQL injection, we can hope that the ORM or something further on down the chain will prevent Bad Stuff from happening. But why even let it get to that point?

[FastAPI](https://fastapi.tiangolo.com/tutorial/query-param-models/#query-parameters-with-a-pydantic-model) does an awesome job of this, thanks to Pydantic models. For example, we can validate a complex set of query parameters before it even hits the controller method. 

```python
class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    # do cool stuff here using our well validated filter_query object
```
Even if the code had a giant SQL injection vulnerability with the limit/offset/order_by parameters, the request isn't going to get that far.

There are other benefits. Because the inputs (and outputs) are well specified, fastAPI can generate an [OpenAPI](https://www.openapis.org/) interface for free. That means a nice UI for testing API endpoints and auto-generation of API client libraries in any language you can think of, among other benefits. (It would be cool if it did GraphQL as well, but nothing's perfect.)

### Validation logic should be a part of the model
In Laravel-land, if there are multiple endpoints that write to the database, there's no guarantee they will all use the same validation rules.

It might be nice if there was only ever one endpoint per data type, but that's not how it works in reality. There might be one endpoint used by the website, another used by the JSON API, and a 3rd used in a mobile app webview, a 4th one on some old promo page everyone forgot about, and a 5th one in an admin tool. And what about loading/syncing data from another datasource via a batch job? Shouldn't that get validated, too? Why is data validation so tightly coupled to the HTTP request/response cycle?

To the framework's credit, you can create an independent `Validator` object in Laravel that isn't tightly coupled to the HTTP request, but the documentation doesn't explain why you'd want to do that (which is always, IMO; the alternative is madness.)

Instead, the official way to do more sophisticated data validation in Laravel is to create a custom HTTP request class called a [Form Request](https://laravel.com/docs/13.x/validation#form-request-validation). Now we're tightly coupling the validation rules not just to HTTP requests, but HTML forms and authorization rules as well. We're moving in the wrong direction! 

Form requests are just a way to move some model logic from the controller class (where it shouldn't be) to a different part of the controller layer (where it also shouldn't be). Keeping controllers "skinny" is one of Laravel's guiding principles, according to founder [Taylor Ottwell](https://laraveldaily.com/post/taylor-otwell-thin-controllers-fat-models-approach). But form requests are just hiding evidence of stuff that shouldn't be in the controller at all.

### Disdain for databases and the N+1 problem
A lot of people who write web apps don't seem to like databases, or really understand them. This leads to a lot of anti-patterns to avoid writing even pretty easy SQL queries. (This certainly isn't unique to Laravel.)

ORMs often display a problem called the "N+1 problem". Fetching a set of data from one model doesn't necessarily load the related data until you need it. You might fetch 100 book records from the database, which is done in a single SQL query. But then, as you print out each book record, it has to do a query to fetch the name of the author of the book from another table. It's trying to save time by not fetching related data you might never use. But if you do need to use it, the system ends up doing 101 queries to get 100 full records.

Laravel provides a way of preventing lazy loading and/or warning when your code is doing it. But eager loading in Laravel is still non-ideal. This Laravel code will avoid the N+1 problem when accessing author data:

```php
<?php

$catBooks = Book::with('author')->where('subject', 'cats')->get();
```

But it still fires off two requests, one to get the Books, then a second request to fetch the authors in bulk by ID. That's not terrible, but the whole point of relational databases is, you know, relations. There's no reason not to get the book and author data in a single query:

```sql
SELECT B.*, A.*
FROM books B
JOIN authors A
ON
    B.author_id = A.id
WHERE
    B.subject = :subjectName
```

### Mighty Morphin' Query Builders
Laravel has a query builder. It's like every other query builder in that its usage is harder to understand, and less performant, than a bit of raw SQL written with knowledge and care. There's no reason to believe that using the query builder is safer than writing a prepared statement by hand. And explaining how to use the query builder takes at least as much work as explaining how SQL works, but you have to write it in an Object-Oriented style instead of declarative.

Here's an example from Laravel's query builder documentation:

```php
<?php

$users = DB::table('users')
    ->where('votes', '>', 100)
    ->orWhere(function (Builder $query) {
        $query->where('name', 'Abigail')
            ->where('votes', '>', 50);
        })
    ->get();
```

The equivalent SQL would be:

```sql
select * 
from users 
where votes > 100 or (name = 'Abigail' and votes > 50)
```

I find it hard to believe that there's anyone who finds the PHP version more readable than the SQL version. If I didn't know any better, I'd think the SQL version was used to generate the less readable PHP version rather than the other way around.

As a database nerd, I've spent a lot of time optimizing slow SQL queries. If the PHP version of the query ends up in the slow query log, it can be a pain to find where in the codebase the query is being built. 

Query builders also encourage developers to scatter complex one-off SQL queries all over the codebase. This makes optimizing database performance a game of whack-a-mole. A much better paradigm is having complex queries written by hand, contained within [Repository pattern](https://www.umlboard.com/design-patterns/repository.html) style classes. That makes optimizing the SQL and caching the results in a standard way much easier.

Laravel's seeming lack of respect for databases shows up in the nomenclature as well. Laravel's "pivot tables" are what everyone else calls ["associative tables"](https://en.wikipedia.org/wiki/Associative_entity), "junction tables" or "join tables" -- a way to record many-to-many relationships between two other tables. They have nothing to do with what everybody else calls pivot tables, the kind you use in Microsoft Excel. Maybe it's *an Albany expression*, but it's absurd, and implies that whoever built the Laravel ORM didn't even know basic stuff about databases.

### This helper function really could have been an if() statement
This is super trivial, which is why it's at the end. But it fits into the larger Laravel ethos of "more is better". Laravel comes with bazillions of little utility functions, some of which are genuinely helpful, others of which have no reason to exist.  Some examples (the actual code is as simple as you think):

* "The `exactly` method determines if the given string is an exact match with another string."
* "If you would like to conditionally dispatch an event, you may use the `dispatchIf` and `dispatchUnless` methods."
* "Append the given values to the string."
* (Paraphrasing) "You can pass an additional function, and if it returns false, the parent won't ever be run."

These are all things that can be done with basic language functionality and control structures even the most beginner programmer should be aware of. We don't need a special Laravel branded version of the `if()` statement or the `===` operator. I don't know who is helped by these trivial functions. As with the bigger issues with authorization and validation, they reflect an odd set of priorities.