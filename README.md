# RecipeRadar TARDIR

Time And Relative Dimensions In Recipes

TARDIR is a collection management and assessment engine for food recipes sourced from the World Wide Web.

## Procedures

### Terms and Conditions Discovery

Absence of terms and conditions for a recipe website in the Common Crawl dataset is **not** a reliable indicator that the website lacks such a policy.  It may simply be the case that the terms document was not found during the CC crawling.

So at best, we can use the tooling provided here to locate cases where terms and conditions **are** found.

We may also be able to highlight particular words or phrases for manual review, but we do not currently plan to automate the determination of whether crawling and caching of content are permitted by any terms and conditions documents found.
