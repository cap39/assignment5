package JavaFiles;
public abstract class RideService {
    protected PricingStrategy pricingStrategy;

    public RideService(PricingStrategy pricingStrategy) {
        this.pricingStrategy = pricingStrategy;
    }

    public abstract double calculateFare(double distance);
}