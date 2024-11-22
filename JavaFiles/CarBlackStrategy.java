package JavaFiles;
public class CarBlackStrategy implements PricingStrategy {
    @Override
    public double calculateFare(double distance) {
        return distance * 2.0; // Example rate per km
    }
}