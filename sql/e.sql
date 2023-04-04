SELECT
  *
FROM "public"."a" AS T1
  LEFT JOIN "public"."d" AS T2
  ON T1."id" = T2."id"
