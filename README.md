# Report Generator

This is a program that chacks input password against a database of hacked passwords provides by https://haveibeenpwned.com/. The input password is converted to a hash key using the SHA1 algorithm and the portion of this key matched against the database via an API. 

Hashing the password before sending ensures that your password is never sent over the net in its raw form.

**Dependencies**
- requests