package JavaFiles;

public class ClientPayment {
    public static void main(String[] args) {
        PaymentService paymentService = new PayPalServiceProxy();

        // Simulating a client making a payment request
        paymentService.processPayment("1234567812345678", 150.0);
        paymentService.processPayment("12345678", 50.0); // Should fail validation
    }
}