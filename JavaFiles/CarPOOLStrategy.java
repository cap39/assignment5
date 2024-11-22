package JavaFiles;
public class CarPOOLStrategy implements PricingStrategy {
    @Override
    public double calculateFare(double distance) {
        return distance * 0.5; // Example rate per km
    }
}