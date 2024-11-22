package JavaFiles;

// PayPalServiceProxy.java
public class PayPalServiceProxy implements PaymentService {
    private PayPalService payPalService;

    public PayPalServiceProxy() {
        this.payPalService = new PayPalService();
    }

    @Override
    public void processPayment(String cardNumber, double amount) {
        if (validate(cardNumber, amount)) {
            logRequest(cardNumber, amount);
            payPalService.processPayment(cardNumber, amount);
        }
    }

    private boolean validate(String cardNumber, double amount) {
        // Basic validation logic
        if (cardNumber == null || cardNumber.length() != 16) {
            System.out.println("Invalid card number.");
            return false;
        }
        if (amount <= 0) {
            System.out.println("Invalid payment amount.");
            return false;
        }
        System.out.println("Validation successful.");
        return true;
    }

    private void logRequest(String cardNumber, double amount) {
        // Log request information before sending to PayPal
        System.out.println("Logging payment request...");
        System.out.println("Card Number: " + cardNumber);
        System.out.println("Amount: $" + amount);
    }
}