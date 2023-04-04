SELECT
  *
FROM "public"."b-1" AS B1
  LEFT JOIN "public"."b-2"
    ON "public"."b-1"."id" = "public"."b-2"."id"
