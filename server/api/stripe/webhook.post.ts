export default defineEventHandler(async (event) => {
  // Catch Stripe webhooks to update user subscription status in your database
  const body = await readRawBody(event)
  // 1. Verify Stripe signature
  // 2. Handle 'checkout.session.completed', 'invoice.paid', etc.
  // 3. Update database: User -> Subscription Tier
  return { received: true }
})
