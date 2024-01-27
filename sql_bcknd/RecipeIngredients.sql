CREATE VIEW RecipeIngredients AS
SELECT *,
RecipeID || IngredientID AS RecipeIngredientKey
FROM RecipeIngredients_STG