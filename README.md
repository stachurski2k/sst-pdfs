# Base Fast API project structure

## Structure overview

### core
Use for most crucial stuff

### exceptions
Use for application wide exceptions

### mappers
Use for creating converters between objects, also its place for adapters

### models
Use for application wide objects. Like db entities or value objects

### repos
Should provide access to DB

### routers
Implementations of API endpoints

### schedulers
Model background logic

### schemas
DTOs

### services
Model business logic

### static 
Application static resources

### templates
Page templates

### utils
Common utilities

### views 
Logic for rendering pages (should be called from routers)

## The structure
![Alt text](/assets-discard/fast-api-base.png)

Controller depends on model and view.

Everything depends on core.




