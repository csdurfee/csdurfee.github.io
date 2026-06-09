Title: Laravel, security and the paradox of choice
Date: 2026-06-01 10:20
Category: software development
Tags: security, Laravel

[!["Don't Explain", Dexter Gordon](https://img.youtube.com/vi/dpjM7wwSTxI/0.jpg)](https://www.youtube.com/watch?v=dpjM7wwSTxI){:target="_blank"}

Song: ["Don't Explain", Dexter Gordon](https://www.youtube.com/watch?v=dpjM7wwSTxI){:target="_blank"}

I've been working with [Laravel](https://www.laravel.com) recently. It's good, probably the best tool for making webapps in PHP right now, for anyone still left doing that. But like any framework, it isn't perfect. It has some very PHP-ish flaws, like misusing established jargon. But the biggest PHP-ish Laravel sin is that there are a bajillion different ways to do every little thing.

Having lots of good choices isn't always better. If I ask you to choose between 10 different flavors of ice cream you like, it may be hard for you to pick one. Do you go with rocky road, or pistachio, or chocolate? They're all good choices. You think about each one, and are happy, then think about the 9 flavors you don't get to have by choosing that one, and are less happy.

If I give you two choices, one you like, and one you hate, you will probably be happier with your decision than if you had 10 good choices. You can feel confident that you picked the right one. There's no chance for regret or second-guessing. That's the paradox of choice. People can end up being less happy if they have too many good options. 

In an engineering context, it's not exactly like picking rocky road and kinda wishing you picked pistachio, but too many options still causes mental overhead. This pops up a lot in Laravel. Let's say you want to get the current user.  You can:

* call `auth()->user`. `auth()` is a helper method that's available everywhere in Laravel.
* call `request()->user`. `request()` is another global helper method.
* call `Auth::user()`. `Auth` is a facade that's also available everywhere.
* have the user passed in by automatic dependency injection, possibly with the help of the `[CurrentUser]` annotation or route model binding
* pass the request through automatic dependency injection, then get the user from that

There are probably others! That's true of basically everything in Laravel.  The documentation will give you 5 different ways to do the same thing and say it's up to you to choose. Maybe it's not a big deal, but who does that help, exactly? 

If there's only one way to do a thing, everybody uses it. In Django, to get the current user, you do `request.user`. In Yii, you do `Yii::$app->user`. There's no need to think about it when reading or writing Django or Yii code, and probably most other frameworks. 

Laravel forces us out of a coding flow state to make trivial choices all over the place. You have to sit down and decide which way you're going to do it instead of just doing it. It's not really a creative choice, or one that makes the software more powerful. It's another thing to think about that doesn't create value for anybody.

It's worse with multiple developers working on a project, especially with AI helpers in the mix. It's bad for maintainability to have everybody doing it their own way, based on their current mood or what they're used to, rather than a good engineering reason. 

Most of the time, Laravel's paradox of choice is a pretty minor issue. It's just a vector for sloppiness, not a fatal flaw. Sometimes the team needs to establish the official way of doing things, though thanks to the Law of Triviality, trying to hash out the One True Way can be an annoying waste of time. 

I wonder how many thousands of developer-hours have been wasted worldwide deciding between "PUT" and "PATCH". I still remember a meeting from 13 years ago where we spent a good half hour debating that issue. It was an internal API, and couldn't have mattered less. People in general, and nerds specifically, tend to get sucked into trivial bikeshedding debates. If the two choices were "PUT" and a bit of eldritch speech that summons the Ancient Gods to devour the world, we'd all be fine with using "PUT", I'm sure. It would've been a short meeting.

## Not knowing what you're doing versus not even trying
It's different when security is involved. What's happening and why needs to be crystal clear. I think it's worth being dogmatic about how security-related code is written.

The [OWASP Top 10](https://owasp.org/Top10/2025/) is a list of the most common types of security problems on the web. It's easy to think of security and envision a zero-day attack on the Linux kernel or some daring social engineering hack, but the vast majority of attacks either fall under the heading of "Not Knowing What We're Doing", or "We're Not Even Trying". 

Anybody who creates software for the web should be hyper-aware of the OWASP Top 10, if only to understand how prosaic most of the issues are. The top two issues in the 2025 list were [Broken Access Control](https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/) and [Security Misconfiguration](https://owasp.org/Top10/2025/A02_2025-Security_Misconfiguration/). Those two are always near the top, and both of them can be affected by having too many choices. 

In order to have a Security Misconfiguration, you have to have a configuration to misconfigure, right? Somebody chose an insecure configuration, or the software wasn't secure out of the box. More moving parts increases the odds of that happening. A certain amount of Security Misconfiguration issues could be eliminated by having fewer things you can do wrong.

Laravel ships with pretty reasonable security defaults, though it's easy to overindex on the wrong things when looking at a list of features. Any good framework should protect you against XSS, CSRF, injection, and mass assignment, which I'd classify as "Not Even Trying" problems at this point. Additional browser security features, like Content-Security-Policy and Same Site cookies, have made it harder to screw things up, even if you misconfigure things, or the framework fails to prevent a problem. Anyone who's actually trying should be pretty well protected against those issues. 

The #1 issue, Broken Access Control, which was also #1 in the previous rankings in 2021, is squarely in the *Not Knowing What We're Doing* category. This is a place where disciplined engineering practices can make a big difference, and where Laravel's "do it however you want, yolo" approach to *everything* doesn't just trigger annoying bikeshedding convos but actual security incidents.

## A maze of twisty passages, all alike.
Authorization is really easy to screw up in the best of conditions. Nobody wakes up and thinks, "I'm gonna do auth wrong today." We try, and we do it wrong. There's a reason why it's the #1 security issue -- it's error prone.

Laravel lets its users down by giving them too many auth-related choices. I'm going to try to enumerate all the ways you can do authorization checks in the latest version of Laravel (13.x). It's a staggeringly long list, and I'm probably missing some. [Official documentation here, if you want to play along at home.](https://laravel.com/docs/13.x/authorization)

You can:

* do it in raw PHP without using the Laravel authZ system at all. The official documentation suggests this.
*  define an access control rule on the fly and then use it in the middle of a controller
*  do it on the fly in the routes file 
*  define model-level policies in the application service provider's `boot()` method (Laravel's junk drawer, ugh)
*  manually register Policy classes in non-standard locations through the `boot()` method as well
*  manually register a policy via a different syntax in `boot()` called a "class callback array"
*  create a Policy class (which is auto-discovered) and check them against the current user/object with the `Gate::` facade
*  use the `->can()` method on the user object to check policies
*  check a policy against the model's class (rather than specific objects) with various methods
*  override a Policy with a policy filter and `Gate::before()`, which supersedes the normal policy checks. 
*  also override policy checks with `Gate::after()`
*  apply policies to controller classes via PHP attributes
*  apply policies through the `can` middleware applied to a single route, by munging the normal arguments to `can()` into a single string (ugh)
*  apply the `can` middleware on a group of routes
*  check permissions in the `authorize()` method of a Form Request
*  show/hide content in the view layer based on policies using the `@can` directive
*  if you are using Laravel Inertia (their framework for single-page webapps), you can also define security policies in the `HandleInertiaRequests` middleware (which uses different syntax than other auth code in Laravel)

If you have both HTML and JSON API endpoints, that can mean two sets of whatever method you choose, with added requirements to exclude database fields you'd never expose through HTML. 

Sheesh. Imagine doing a security audit on a Laravel application. You'd have to check every one of those possibilities to understand/document how the system does auth, then figure out if it's working as intended. 

As with Laravel's other "choose your own adventure" options, it appears that all the above methods are using the same basic code. The framework hasn't dramatically increased the complexity/attack surface of their own code, but they have yours. How can we understand whether authorization is being applied the way it's *supposed to*. when there are so many possible ways to apply the rules?

## Remediations & recommendations
Laravel has a nice event system. It fires off an event called [`GateEvaluated`](https://github.com/laravel/framework/commit/0c6f5f75bf0ba4d3307145c9d92ae022f60414be) every time that an authorization policy is checked. It would be pretty easy to log every auth check performed by Laravel, but it's not going to be all that helpful without some curation.

For instance, frontend code might use the `@auth` directive to decide whether to display an edit link on a piece of content. If only the owner is allowed to edit it, the vast majority of the time, the edit link shouldn't display and that check is going to fail. It doesn't mean that someone is trying to hack the system. So failed auth checks are going to have a lot of noise.

Granular auth checks can help separate signal from noise, and are a good idea anywhere. For instance, there should be separate policies for `can edit` (used to gate access to the edit page, or saving edits) and `can view edit link` (prevent showing the link to the edit page). `can view edit link` failures are probably not a result of user misbehavior.

We should be more concerned about the dog that didn't bark. The logs can't tell you that an auth check should have failed, but passed instead. A log of auth checks would be valuable for incident response after something bad has happened, but you can't really use it to proactively find problems. Pathways that lead to circumvention of auth rules shouldn't happen during normal use of the system.

The question of "should person A be allowed to do action B to thing C?" is a business logic question. Somebody or something has to know how the business should work to recognize the code's not working right. That requires a certain amount of manual auditing of the codebase, and a [single source of truth](https://en.wikipedia.org/wiki/Single_source_of_truth). If authorization rules are defined and checked in a standard way, that's a whole lot easier to do.

### Start with policy classes and RBAC
Laravel's [Policy classes](https://laravel.com/docs/13.x/authorization#creating-policies) are a good way to make sure that authorization rules are defined in predictable locations for a particular Model. I would recommend using them from the beginning of a project.

Laravel has an ACL-based security model. It's worth starting with [Role Based Access Control](https://en.wikipedia.org/wiki/Role-based_access_control) from the beginning, and it's odd the framework doesn't come with it out of the box, considering frameworks like Symfony and Django do. Spatie's [laravel-permission](https://spatie.be/docs/laravel-permission/v8/introduction) package looks like a much better choice than rolling your own.

For policies that aren't tied to a particular model, such as who can access `/admin` type pages, you can define Policy classes that aren't tied to a particular model, then register them in the `boot()` method of the app. That keeps all policies in one standard location.

As far as checks against those policies, explicitly using the `Gate::` functions everywhere makes findability easier. Finding every auth check being done in the system shouldn't be some kind of treasure hunt.

The `user()->can()` syntax is convenient but can't apply to all auth situations. Consistent checking is less important than clear definition of permissions, though. Can I search for the name of the permission and find everywhere in the code using it? Can I see which role(s) the permissions are assigned to? Can I see which users have that role, and maybe some clue why they're in that role? Are the permissions granular enough, and have they been assigned following least privilege?

Laravel `FormRequest`s are the framework's one nod to more sophisticated security. They offer a mechanism to combine authorization and validation in one object. I'm not a huge fan of them because data validation should be a Model level concern, not a Controller level one. There's no good reason why validation should be tightly coupled to HTTP and HTML forms, except for the curious nature of Laravel models. (More on that next week.) While `FormRequest`s are odd from an architecture standpoint, consistent use of them is certainly better than a scattershot approach to auth. Keep things simple and consistent if you possibly can.