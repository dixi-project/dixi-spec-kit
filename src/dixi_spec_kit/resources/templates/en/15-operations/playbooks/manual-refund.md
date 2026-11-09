# Manual refund

## Purpose

Return money to a customer outside the automatic flow in a controlled, traceable way, with the right approvals and no double refunds.

Status: draft. {{pending: name the owner of this playbook}}

## When it applies

- A charge failed to be reversed automatically.
- An incident caused wrong charges for one or many customers.
- A support agreement or goodwill decision grants a refund.

## Rules

- Refunds go back to the original payment method unless the policy says otherwise. {{pending: define exceptions}}
- Every refund has a reason code and a link to the ticket or incident.
- Approval limits: {{pending: amount}} support lead; above that, finance contact.
- The person who requests a refund is not the one who approves it.
- An AI agent may prepare the list and the evidence; a person approves and executes.

## Single refund

1. Check the original charge, the amount already refunded and the customer's account state.
2. Confirm the reason and the amount with the ticket owner.
3. Get approval according to the limits above.
4. Issue the refund in the payment tool. {{pending: name the tool role, not the vendor}}
5. Record the refund ID, amount, reason and approver.
6. Notify the customer with the expected arrival time.

## Batch refund (after an incident)

1. Build the list of affected charges from logs or the database with a reviewed, read-only query.
2. Have a second person check the list: totals, duplicates, already refunded items.
3. Run a small pilot of {{pending: number}} refunds and verify them.
4. Run the rest in small batches, stopping at the first unexpected error.
5. Reconcile: total refunded equals total approved.

## Close criteria

- All approved refunds issued and reconciled.
- Customers notified.
- Accounting informed of the total and the reason. {{pending: how accounting is informed}}

## Related

- [Support model](../support-model.md)
- [Incident levels](../incident-levels.md)
- [Customer outage communication](comms-outage-customer.md)
- [RACI matrix](../team/raci-matrix.md)
