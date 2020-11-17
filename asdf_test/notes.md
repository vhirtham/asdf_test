# ASDF notes

## File structure

- optional index list at the end of the file. Consists of integers that provide the position of the first character of 
each binary data block. The index refers to the beginning of the file.

## `AsdfFile` class

### Creating an instance
Steps (ignoring simple checks):
1. load extensions - can either be a `AsdfExtensionList` or a class that inherited from `AsdfExtension`. An 
`AsdfExtensionList` is simply stored in `_extensions`. If it is an `AsdfExtension` the following happens:
    - `('', '')` is stored an meta data in the `_extension_metadata` dictionary using the extension name as key
    - Creates an `AsdfExtensionList` from the provided extension and the default extensions and stores it in 
    `_extensions`
    - Add the meta data of the default extensions to `_extension_metadata`
2. load custom schema for file using a special ASDF loader
    - the url is updated to the absolute path
    - the content of the schema is returned as dictionary
    
#### Questions and Answers:

**Where is the data about available (custom) types stored?**

In the private member `_extensions.type_index` a set of metadata about all known types is stored.

**Where is a custom schema validated?**

The validation is hidden in the assignment of the tree `self.tree = tree`. This calls a setter!

**What tag does a custom schema need and why?**

There shouldn't be a tag in a custom schema. If a tag is present, it will be validated against the tag
`"tag:stsci.edu:asdf/core/asdf-1.1.0"`. The reason for this is, that tree that should be serialized is wrapped by an
`AsdfObject` class. The tag corresponds to that class.



## `write_to`

Steps (ignoring simple checks):
- pre write step 
    - running `pre_write` hooks of custom classes
    - add asdf version information to the tree using the key "asdf_library" and the value being an instance of a 
    special `Software` class
    - update the extension history using the "history" key is the tree.
- serial writing step
    - write tree substep
        - write the file header first
        - dump the tree
            - decode the tag of the tree
            - turn tree into tagged tree
            - validate the tree
            - remove all entries that have default values (check what happens during loading if a required value was removed)
        
~~~ python
    tree = custom_tree_to_tagged_tree(tree, ctx)
    schema.validate(tree, ctx)
    schema.remove_defaults(tree, ctx)
~~~

## Resolvers

Resolvers are just wrappers for different methods to map an input string with a specific prefix 
to an output string. Currently, two kinds of mappings are supported:
- a tuple that stores the input and output value of the mapping
- a function with a single parameter (string) that returns a string or `None`

## ResolverChain

A class that contains multiple Resolvers that are chained together. Each resolver gets the output of the previous
resolver as input.


## Special Functions

### walk_and_modify

Traverses the whole tree recursively and calls a callback function for each node.
- the traversal order can be selected using the `postorder` parameter
- it caches the callback results for each node. If the node is found somewhere else the cached results are used
- the callback needs the following parameters: `(node)` or `(node, json_id)` where the returned value is the new 
node value



## Misc

- there is a serializable `Software` class in asdf