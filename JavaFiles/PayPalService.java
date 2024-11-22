package JavaFiles;
// PayPalService.java
public class PayPalService implements PaymentService {
    @Override
    public void processPayment(String cardNumber, double amount) {
        System.out.println("Processing payment with PayPal...");
        System.out.println("Card Number: " + cardNumber);
        System.out.println("Amount: $" + amount);
        // Here we would interact with the PayPal API
    }
}
