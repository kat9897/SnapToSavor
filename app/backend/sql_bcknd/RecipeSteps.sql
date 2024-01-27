CREATE VIEW "RecipeSteps" AS
SELECT *,
RecipeID || StepOrder AS RecipeStep
 FROM RecipeSteps_STG