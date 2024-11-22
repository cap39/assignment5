package JavaFiles;
public class CarXStrategy implements PricingStrategy {
    @Override
    public double calculateFare(double distance) {
        return distance * 1.0; // Example rate per km
    }
}
